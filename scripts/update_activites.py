#!/usr/bin/env python3
"""Met à jour les images de la page Activités :
- remplace 7 images externes par des versions libres de droits auto-hébergées (alt corrigés) ;
- conserve 3 images externes (sujets hyper-locaux introuvables en libre) avec alt corrigé."""
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "activites", "index.html")

with open(path, encoding="utf-8") as f:
    html = f.read()

# (sous-chaîne unique du src actuel, nouveau src ou None pour conserver, nouvel alt)
mapping = [
    ("photo-1438755582627", "../public/activites/bambouseraie.webp",
     "Bambous de la Bambouseraie d'Anduze"),
    ("photo-1596458162315", "../public/activites/pont-du-gard.webp",
     "Le Pont du Gard, aqueduc romain classé à l'UNESCO"),
    ("pret-a-partir.jpg", "../public/activites/train-vapeur-cevennes.webp",
     "Train à Vapeur des Cévennes"),
    ("8310254.jpg", "../public/activites/grotte-trabuc.webp",
     "Lac souterrain de la Grotte de Trabuc"),
    ("rando-cevennes-6", "../public/activites/sentiers-cevennes.webp",
     "Paysage de la Corniche des Cévennes"),
    ("photo-1519092796169", "../public/activites/vins-cevennes.webp",
     "Dégustation de vins des Cévennes"),
    ("dsc-0275.jpg", None, "Marché nocturne d'Anduze en été"),
    ("64d74620291dc031507f5c4c", None, "Marché du jeudi matin à Anduze"),
    ("Velorail-Thoiras", None, "Vélorail de Thoiras dans les Cévennes"),
    ("20893954.jpg", "../public/activites/poterie-anduze.webp",
     "Poterie et jarres d'Anduze"),
]


def rebuild(m):
    tag = m.group(0)
    entry = next((e for e in mapping if e[0] in tag), None)
    if not entry:
        return tag
    _sub, newsrc, alt = entry
    cur = re.search(r'src="([^"]+)"', tag).group(1)
    src = newsrc if newsrc else cur
    return (
        '<img\n'
        '            loading="lazy"\n'
        f'            src="{src}"\n'
        f'            alt="{alt}"\n'
        '            class="activites__activite--img"\n'
        '          />'
    )


new_html, n = re.subn(
    r'<img\b[^>]*?class="activites__activite--img"[^>]*?/>',
    rebuild, html, flags=re.S,
)
with open(path, "w", encoding="utf-8") as f:
    f.write(new_html)
print("Images d'articles traitées :", n)
print("Restées externes :", sum(1 for e in mapping if e[1] is None))
print("Auto-hébergées   :", sum(1 for e in mapping if e[1] is not None))
