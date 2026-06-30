#!/usr/bin/env python3
"""Génère des variantes responsive WebP pour la galerie et recompresse les images d'accueil.

- Galerie (public/photo/IMG_*.webp) : originaux conservés intacts, génère _400px/_800px/_1600px.
- public/presentation_*px.webp : recompressés sur place (correctif LCP).
- public/activites.webp : recompressé sur place.
"""
import os
import re
import glob
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO_DIR = os.path.join(ROOT, "public", "photo")
SIZES = [400, 800, 1600]
QUALITY = 80
METHOD = 6

variant_re = re.compile(r"_\d+px\.webp$")


def kb(path):
    return os.path.getsize(path) // 1024


def gen_gallery():
    originals = [
        f for f in glob.glob(os.path.join(PHOTO_DIR, "*.webp"))
        if not variant_re.search(f)
    ]
    print(f"== Galerie : {len(originals)} originaux ==")
    for src in sorted(originals):
        base = src[:-5]  # retire .webp
        with Image.open(src) as im:
            im = im.convert("RGB")
            ow = im.width
            for w in SIZES:
                target = min(w, ow)
                r = im.copy()
                r.thumbnail((target, target * 100), Image.LANCZOS)
                out = f"{base}_{w}px.webp"
                r.save(out, "WEBP", quality=QUALITY, method=METHOD)
        name = os.path.basename(base)
        print(f"  {name}: {ow}px -> "
              + ", ".join(f"{w}px={kb(base+f'_{w}px.webp')}Ko" for w in SIZES))


def recompress_inplace(pattern_or_path):
    paths = glob.glob(pattern_or_path) if "*" in pattern_or_path else [pattern_or_path]
    for f in sorted(paths):
        if not os.path.exists(f):
            continue
        before = kb(f)
        with Image.open(f) as im:
            im = im.convert("RGB")
            im.save(f, "WEBP", quality=QUALITY, method=METHOD)
        print(f"  {os.path.basename(f)}: {before}Ko -> {kb(f)}Ko")


if __name__ == "__main__":
    gen_gallery()
    print("== Recompression presentation_*px.webp ==")
    recompress_inplace(os.path.join(ROOT, "public", "presentation_*px.webp"))
    print("== Recompression activites.webp ==")
    recompress_inplace(os.path.join(ROOT, "public", "activites.webp"))
    print("FINI")
