# Audit SEO complet — villaanduze.fr

> Date : 30 juin 2026
> Méthode : analyse du site en ligne (https://villaanduze.fr) **+** inspection du code source du dépôt.
> Périmètre : 5 pages (Accueil, Photos, Équipements, Activités, Contact).

---

## 1. Résumé exécutif

| Indicateur | Valeur |
|---|---|
| **Score de santé SEO global** | **42 / 100** — *À améliorer* |
| Type d'activité détecté | **Hébergement touristique local** (gîte / location de vacances) — établissement physique à Anduze (30140), Gard, Cévennes |
| Hébergement | Hostinger / LiteSpeed — site statique déployé tel quel (pas de build Vite en production) |
| Pages indexables | 5 |
| HTTPS | ✅ actif, redirection HTTP→HTTPS OK |

### Décomposition du score

| Catégorie | Poids | Score | Pondéré |
|---|---|---|---|
| SEO technique | 22 % | 45/100 | 9,9 |
| Qualité de contenu | 23 % | 60/100 | 13,8 |
| SEO on-page | 20 % | 42/100 | 8,4 |
| Données structurées (Schema) | 10 % | 0/100 | 0,0 |
| Performance (Core Web Vitals) | 10 % | 40/100 | 4,0 |
| Préparation IA / GEO | 10 % | 35/100 | 3,5 |
| Images | 5 % | 55/100 | 2,75 |
| **TOTAL** | **100 %** | | **≈ 42/100** |

### 🔴 Top 5 des problèmes critiques

1. **Aucune donnée structurée (Schema.org).** Pour un hébergement, l'absence de `LodgingBusiness`/`VacationRental` + `LocalBusiness` prive le site des résultats enrichis Google et des citations IA. Impact direct sur la visibilité locale.
2. **Titre `<title>` identique sur les 5 pages** : « Villa 'nduzienne ». Aucun mot-clé, aucune localisation. Google ne peut pas différencier ni positionner les pages.
3. **Meta description identique sur les 5 pages** (copie de celle de l'accueil). Duplication on-page massive.
4. **robots.txt et sitemap.xml absents (HTTP 404).** Aucune directive de crawl, aucun plan du site soumis aux moteurs.
5. **Contenu dupliqué www / non-www** : `www.villaanduze.fr` et `villaanduze.fr` servent un contenu **identique sans redirection ni canonical**. Dilution du référencement.

### 🟢 Top 5 des quick wins (gains rapides)

1. Réécrire les 5 `<title>` et 5 meta descriptions (uniques, avec « gîte / Anduze / Cévennes / piscine »). ~1 h.
2. Ajouter le bloc JSON-LD `LodgingBusiness` sur l'accueil et `LocalBusiness` sur Contact (fournis dans l'ACTION-PLAN). ~1 h.
3. Créer `robots.txt` + `sitemap.xml` (contenus prêts à coller fournis). ~15 min.
4. Ajouter une balise `<link rel="canonical">` sur chaque page + redirection 301 www→non-www via `.htaccess`. ~30 min.
5. Corriger le lien téléphone cassé sur Contact (`tel:9051290512` ≠ numéro affiché). ~2 min.

---

## 2. SEO technique — 45/100

### Crawlabilité & indexabilité
- 🔴 **robots.txt → HTTP 404.** Le serveur renvoie une page HTML générique d'erreur au lieu d'un vrai fichier. Aucune directive, aucune référence au sitemap.
- 🔴 **sitemap.xml → HTTP 404.** Inexistant.
- 🔴 **Aucune balise canonical** sur aucune page.
- 🟢 Toutes les pages répondent en **HTTP 200**, structure d'URL propre et lisible (`/photos/`, `/equipements/`, `/activites/`, `/contact/`).
- 🟢 `lang="fr"` présent, `<meta viewport>` présent → mobile-friendly de base.

### Duplication de domaine
- 🔴 **`www.villaanduze.fr` renvoie un contenu strictement identique** (MD5 identique) **sans redirection**. Risque de contenu dupliqué et de dilution. → Mettre en place une redirection 301 vers la version canonique (non-www recommandé) + canonical absolu.

### Sécurité & en-têtes HTTP
- 🟢 HTTPS actif, HTTP→HTTPS en 301, en-tête `Content-Security-Policy: upgrade-insecure-requests`.
- 🟡 **Aucun en-tête de sécurité** notable : pas de `Strict-Transport-Security` (HSTS), `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.
- 🟡 **Aucun en-tête de cache** (`Cache-Control` / `Expires`) sur les assets statiques (CSS, JS, images) → pas de mise en cache navigateur optimisée, alors que ce sont des fichiers versionnés (`index-v1.6.css`).
- 🟡 **`.htaccess` vide** : aucune des optimisations ci-dessus (cache, compression, redirections, headers) n'est configurée alors que LiteSpeed les supporte.

### Favicon
- 🟡 **`/favicon.ico` (chemin racine demandé par défaut par les navigateurs) → 404.** Le fichier existe mais sous `/public/favicon.ico`. La page d'accueil le référence en `public/favicon.ico` (OK), mais les sous-pages ne déclarent que `favicon.svg`, et la requête racine automatique échoue.

---

## 3. Qualité de contenu — 60/100

### E-E-A-T (Expérience, Expertise, Autorité, Confiance)
- 🟢 **Pertinence locale forte** : champ lexical « gîte / Anduze / Cévennes / piscine / vue / famille » bien présent.
- 🟢 Page **Équipements très complète** (≈ 60 équipements détaillés : Starlink, clim, piscine sécurisée, cuisine équipée…). Excellent signal de valeur pour l'utilisateur.
- 🟢 Page **Activités riche** (11 activités locales avec liens vers sites officiels : Bambouseraie, Pont du Gard, Train à vapeur, Grotte de Trabuc…). Bon maillage sortant d'autorité.
- 🟢 Page **Contact** : tarif (280 €/nuit pour 6 pers.), horaires, téléphone, mail, carte. Bons signaux de confiance.
- 🔴 **Aucune section « à propos / l'hôte »** : pas d'identité du propriétaire, pas d'histoire, ce qui pénalise l'« Experience » et la confiance.
- 🔴 **Pas d'adresse postale visible** (seulement une carte centrée sur Anduze). NAP incomplet.
- 🟡 **Avis** : uniquement un lien sortant vers Google. Aucun avis affiché/structuré sur le site (les avis sont un signal majeur en hôtellerie).

### Contenu mince & duplication
- 🔴 **Meta description identique** sur les 5 pages.
- 🟡 Page d'accueil un peu mince en texte (2 courts paragraphes) ; l'essentiel de la valeur est sur Équipements/Activités.
- 🟡 **Fautes / coquilles** : « Calendrier des réservation » (→ réservations), « Cuisive » (→ Cuisine), « vue sure Peyremale » (→ sur), « marché nocture » (→ nocturne), « Équipements d'entretiens » (→ d'entretien), « Ballade » (→ Balade). Affecte le professionnalisme perçu.

---

## 4. SEO on-page — 42/100

### Balises `<title>`
- 🔴 **Identiques sur les 5 pages** : « Villa 'nduzienne ». 
  - Aucun mot-clé métier ni géographique.
  - L'apostrophe stylisée (`'nduzienne`) nuit à la reconnaissance de la marque par les moteurs.
- → Voir ACTION-PLAN pour 5 titres réécrits.

### Meta descriptions
- 🔴 Identiques sur les 5 pages.

### Structure des titres (Hn)
- 🔴 **Page d'accueil = deux `<h1>`** : un `<h1 class="sr-only">Villa Anduzienne</h1>` + `<h1 class="header__nav--title">Villa 'nduzienne</h1>`. Un seul H1 par page recommandé.
- 🟡 **Sur toutes les pages, le `<h1>` est la marque** (dans l'en-tête), et le vrai sujet de la page n'est qu'un `<h2>` (« Nos Équipements », « Contactez-nous », « Découvrez Notre Gîte en Images »). Le H1 devrait porter le sujet/les mots-clés de la page, pas la marque répétée à l'identique partout.
- 🟢 Hiérarchie H2/H3 cohérente sur Équipements et Activités.

### Open Graph & partage social
- 🔴 **Aucune balise Open Graph** (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) ni Twitter Card. Les partages (WhatsApp, Facebook, Messenger — courants pour une location) s'afficheront sans visuel ni titre soigné.

### Maillage interne
- 🟢 Navigation principale cohérente (5 liens) présente sur toutes les pages, ancres claires.
- 🟡 Peu de liens contextuels dans le corps (ex. depuis l'accueil vers Équipements/Photos/Contact avec ancres optimisées).

---

## 5. Données structurées (Schema.org) — 0/100

- 🔴 **Aucun balisage JSON-LD / microdata sur l'ensemble du site.**
- Opportunités majeures pour un hébergement :
  - `LodgingBusiness` ou `VacationRental` (accueil) : nom, géolocalisation, équipements (`amenityFeature`), capacité, prix, image.
  - `LocalBusiness` + `PostalAddress` + `geo` (contact) : NAP structuré pour le pack local.
  - `AggregateRating` / `Review` si vous rapatriez les avis Google.
  - `ImageGallery` / `ImageObject` (page Photos).
  - `BreadcrumbList` (fil d'Ariane) sur les sous-pages.
- → Bloc JSON-LD complet prêt à coller fourni dans l'ACTION-PLAN.

---

## 6. Performance (Core Web Vitals) — 40/100

### LCP (Largest Contentful Paint) — point faible principal
- 🔴 **Image splash d'accueil non optimisée pour le LCP** :
  - `srcset` jusqu'à `presentation_2560px.webp` (**7 Mo**) ; sur un écran 1920px le navigateur charge `presentation_1920px.webp` = **4,4 Mo** (vérifié en ligne).
  - **Aucun attribut `sizes`** → le navigateur suppose `100vw` et peut surcharger.
  - **Pas de `width`/`height`** → risque de **CLS** (décalage de mise en page).
  - **Pas de `fetchpriority="high"` ni de preload** sur l'image LCP, alors qu'elle est juste sous le pli.

### Ressources bloquantes
- 🟡 **Google Fonts** chargées via `<link rel="stylesheet">` bloquant le rendu (deux familles, plages de poids complètes `100..900`). `preconnect` présent (bien) mais pas de `display=swap` côté `<link>`… *(en réalité `&display=swap` est présent dans l'URL — OK)*. Réduire les poids chargés.
- 🟡 CSS chargé en `<link>` standard (bloquant) — acceptable vu la petite taille (8 Ko).

### Tiers (third-party)
- 🟡 **Iframe Google Calendar** (accueil) et **iframe Google Maps** (contact) : lourds, mais `loading="lazy"` présent → impact limité.

### Poids des médias (dépôt)
- 🔴 **Dossier `public/photo` = 138 Mo.** Images pleine résolution démesurées : `IMG_9920.webp` **11,6 Mo**, `IMG_9914.webp` 11,4 Mo, `IMG_0328.webp` 10,6 Mo, plusieurs 5–7 Mo.
  - En galerie, les vignettes utilisent bien les versions `_400px` (≈ 45 Ko) via `srcset` → chargement initial maîtrisé. **Mais** la lightbox (`modale.js`) ouvre l'image **pleine résolution** (`src`) au clic → jusqu'à **11 Mo par clic**.
- 🔴 **Vidéo** `VID_0001.webm` = **18,7 Mo** (+ `.MP4` 15 Mo) servie sans version allégée.
- 🟢 Format **WebP** utilisé partout (bien), `loading="lazy"` sur la galerie (bien).

---

## 7. Images — 55/100

- 🟢 **Attributs `alt` présents** sur la quasi-totalité des images (bonne base d'accessibilité/SEO).
- 🟢 Format WebP + `srcset` responsive sur l'accueil, lazy-loading en galerie.
- 🔴 **`alt` erronés/dupliqués** sur la page Activités : « La foule durant le marché nocture » est réutilisé pour le **Vélorail**, la **Poterie** et le **Marché du jeudi** (alt copié-collé sans rapport avec l'image).
- 🟡 Coquilles dans plusieurs `alt` (« Cuisive », « vue sure Peyremale »).
- 🔴 **Aucun `width`/`height`** sur les images → CLS.
- 🔴 **Images pleine résolution surdimensionnées** (jusqu'à 11 Mo) à recompresser/redimensionner (cible : ≤ 1920px de large, < 300 Ko).
- 🔴 **Page Activités : images externes en hotlink** (Unsplash, TripAdvisor, apidae-tourisme, midilibre, ales.fr, hit-occitanie, ucia-anduze…). Risque de liens morts, perte de contrôle, performance variable et droits d'usage incertains. → Héberger des visuels en propre.

---

## 8. Préparation IA / GEO — 35/100

- 🔴 **Pas de `llms.txt`** (HTTP 404).
- 🔴 **Pas de données structurées** → les moteurs génératifs (AI Overviews, ChatGPT Search, Perplexity) s'appuient fortement sur le balisage et un NAP clair pour citer un établissement.
- 🟢 **Contenu factuel et bien structuré** (listes d'équipements, activités avec descriptions courtes) → bon potentiel de « citabilité » par passage.
- 🟡 **Signaux d'entité incomplets** : nom de marque instable (« Villa 'nduzienne » / « Villa Anduzienne » / « Villa Anduze » / domaine villaanduze.fr), pas d'adresse complète, pas d'`Organization`/`sameAs` (Google Business, réseaux sociaux).
- → Recommandations : harmoniser le nom de marque, ajouter le balisage `LodgingBusiness`, publier un `llms.txt`, afficher un NAP complet et cohérent.

---

## 9. Inventaire des pages

| URL | Statut | Title (actuel) | H1 | Meta desc. | Schema |
|---|---|---|---|---|---|
| `/` | 200 | Villa 'nduzienne | **2× H1** (marque) | générique | ❌ |
| `/photos/` | 200 | Villa 'nduzienne *(dup.)* | marque | générique *(dup.)* | ❌ |
| `/equipements/` | 200 | Villa 'nduzienne *(dup.)* | marque | générique *(dup.)* | ❌ |
| `/activites/` | 200 | Villa 'nduzienne *(dup.)* | marque | générique *(dup.)* | ❌ |
| `/contact/` | 200 | Villa 'nduzienne *(dup.)* | marque | générique *(dup.)* | ❌ |

---

*Plan d'action priorisé avec correctifs prêts à coller → voir [ACTION-PLAN.md](ACTION-PLAN.md).*
