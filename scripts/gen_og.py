#!/usr/bin/env python3
"""Génère l'image Open Graph (1200x630) dans le style « splash » du site.

Fond : photo piscine + vue Cévennes. Surimpression : dégradé sombre pour la
lisibilité, titre Antonio blanc, accent magenta (#9b1c58) de la charte, et le
nom de domaine. Police variables Antonio/Montserrat (OFL) attendues dans /tmp/vog.

Sortie : public/og-image.jpg
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630
MAGENTA = (155, 28, 88)  # #9b1c58
WHITE = (250, 250, 250)  # #FAFAFA

BG_SRC = os.path.join(ROOT, "public", "photo", "IMG_0003_1600px.webp")
ANTONIO = "/tmp/vog/Antonio.ttf"
MONTS = "/tmp/vog/Montserrat.ttf"
OUT = os.path.join(ROOT, "public", "og-image.jpg")


def font(path, size, weight):
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


# --- Fond : cover-crop centré vers 1200x630 ---
im = Image.open(BG_SRC).convert("RGB")
scale = max(W / im.width, H / im.height)
im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
left = (im.width - W) // 2
top = (im.height - H) // 2
im = im.crop((left, top, left + W, top + H))

# --- Dégradé sombre bas + voile léger global ---
overlay = Image.new("L", (1, H), 0)
for y in range(H):
    t = y / H
    # transparent en haut, opaque en bas
    val = int(165 * max(0, (t - 0.32) / 0.68) ** 1.4) + 28
    overlay.putpixel((0, y), min(val, 200))
overlay = overlay.resize((W, H))
black = Image.new("RGB", (W, H), (0, 0, 0))
im = Image.composite(black, im, overlay)

draw = ImageDraw.Draw(im)
PAD = 70

title = "VILLA 'NDUZIENNE"
sub = "Gîte avec piscine & vue sur les Cévennes · Anduze"
f_title = font(ANTONIO, 100, 700)
f_sub = font(MONTS, 34, 600)

# Bloc texte ancré en bas, espacement maîtrisé
GAP = 26
BOTTOM = H - 62
tb = draw.textbbox((0, 0), title, font=f_title)
sb = draw.textbbox((0, 0), sub, font=f_sub)
title_h = tb[3] - tb[1]
sub_h = sb[3] - sb[1]
sub_top = BOTTOM - sub_h
title_top = sub_top - GAP - title_h

# Titre (Antonio) + ombre portée
draw.text((PAD, title_top - tb[1] + 4), title, font=f_title, fill=(0, 0, 0))
draw.text((PAD, title_top - tb[1]), title, font=f_title, fill=WHITE)

# Sous-titre (Montserrat) + ombre portée
draw.text((PAD + 2, sub_top - sb[1] + 2), sub, font=f_sub, fill=(0, 0, 0))
draw.text((PAD, sub_top - sb[1]), sub, font=f_sub, fill=WHITE)

# --- Domaine en haut à droite, badge magenta ---
f_dom = font(MONTS, 28, 700)
dom = "villaanduze.fr"
bbox = draw.textbbox((0, 0), dom, font=f_dom)
dw, dh = bbox[2] - bbox[0], bbox[3] - bbox[1]
bx2, by1 = W - PAD + 18, 44
draw.rounded_rectangle([bx2 - dw - 36, by1, bx2, by1 + dh + 26],
                       radius=10, fill=MAGENTA)
draw.text((bx2 - dw - 18, by1 + 11), dom, font=f_dom, fill=WHITE)

im.save(OUT, "JPEG", quality=86, optimize=True, progressive=True)
print(f"OK -> {OUT}  {W}x{H}  {os.path.getsize(OUT)//1024}Ko")
