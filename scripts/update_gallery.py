#!/usr/bin/env python3
"""Met à jour les <img> de la galerie photos : srcset 400w/800w + sizes + data-large (1600px),
src allégé en 400px, et corrige quelques fautes dans les alt."""
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "photos", "index.html")

with open(path, encoding="utf-8") as f:
    html = f.read()

alt_fix = {
    "Terrasse avec vue sure Peyremale": "Terrasse avec vue sur Peyremale",
    "Cuisive et salle à manger": "Cuisine et salle à manger",
}

pattern = re.compile(
    r'<img\s+srcset="\.\./public/photo/([A-Za-z0-9_]+)_400px\.webp"\s+'
    r'loading="lazy"\s+'
    r'src="\.\./public/photo/\1\.webp"\s+'
    r'alt="([^"]*)"\s+'
    r'class="gallery__frame--picture"\s*/>'
)


def repl(m):
    name = m.group(1)
    alt = alt_fix.get(m.group(2), m.group(2))
    return (
        '<img\n'
        '            srcset="\n'
        f'              ../public/photo/{name}_400px.webp 400w,\n'
        f'              ../public/photo/{name}_800px.webp 800w\n'
        '            "\n'
        '            sizes="(max-width: 768px) 50vw, 400px"\n'
        '            loading="lazy"\n'
        f'            src="../public/photo/{name}_400px.webp"\n'
        f'            data-large="../public/photo/{name}_1600px.webp"\n'
        f'            alt="{alt}"\n'
        '            class="gallery__frame--picture"\n'
        '          />'
    )


new_html, n = pattern.subn(repl, html)
with open(path, "w", encoding="utf-8") as f:
    f.write(new_html)
print("Balises img galerie mises à jour :", n)
