# Famille T — Typographie française

Référentiel normatif et patterns de correction. Sources : Lexique des règles typographiques en usage à l'Imprimerie nationale (LRTUIN), Banque de dépannage linguistique de l'OQLF, Académie française (QDL005), conventions typographiques de Wikipédia FR, Le Robert.

## Les trois lois de la famille T

1. **Ne jamais dégrader.** Aucune conversion « » → ", ’ → ', espace insécable → sécable, É → E, virgule décimale → point. Une humanisation qui abîme la typographie française est une régression, quel que soit le registre.
2. **Normaliser selon le registre.** Académique/professionnel : typographie exigée. LinkedIn/casual : on tolère l'existant, on n'impose pas — mais on ne casse rien, et l'orthographe (accents sur majuscules) reste due partout.
3. **Respecter la variété.** fr-FR, fr-CA (OQLF) et fr-CH ont des règles d'espacement différentes et toutes légitimes. Détecter la variété du texte (indices : courriel/cégep/$ CA → fr-CA) et ne JAMAIS convertir de l'une vers l'autre.

## Table Unicode de référence

Les caractères de la colonne « Caractère » sont les VRAIS codes (vérifiables à l'octet — les insécables sont invisibles à l'œil).

| Caractère | Code | Rôle |
|---|---|---|
| « » | U+00A0 | Espace insécable (entre ces guillemets) : avant `:`, dans « », avant %, unités, milliers, € |
| « » | U+202F | Espace fine insécable (entre ces guillemets) : avant `; ! ?` (fr-FR), intérieur des « » en composition soignée |
| « » | U+00AB / U+00BB | Guillemets français, 1ᵉʳ niveau de citation |
| “ ” | U+201C / U+201D | Guillemets anglais : 2ᵉ niveau de citation UNIQUEMENT (sans espaces intérieures) |
| ’ | U+2019 | Apostrophe typographique — la seule correcte en français soigné |
| ' | U+0027 | Apostrophe droite (dactylographique) — tolérée chat/code, jamais en print |
| — | U+2014 | Tiret cadratin : dialogues, incises (avec espaces) |
| – | U+2013 | Tiret demi-cadratin : incises (usage éditorial moderne) |
| - | U+002D | Trait d'union : mots composés, intervalles en usage français courant (1914-1918) — JAMAIS une incise |
| … | U+2026 | Points de suspension (préférable à `...` en soigné) |

U+00A0 et U+202F sont invisibles dans un diff : les traiter comme significatifs, les préserver octet pour octet. Si le texte source utilise U+202F, ne pas rétrograder en U+00A0 (ni l'inverse sans raison de registre).

## Règles par objet

### Guillemets
- 1ᵉʳ niveau : « … » avec espace insécable (U+00A0, ou fine U+202F en print) après « et avant ».
- 2ᵉ niveau (citation dans la citation) : “ … ” sans espaces intérieures (consensus moderne FR + OQLF).
- Convertir "..." → « … » en académique/professionnel, premier niveau seulement. Jamais dans le code, les chaînes, les commandes, le JSON/CSV.
- Citations longues sur plusieurs paragraphes avec ouvrant répété : règle LRTUIN correcte, ne pas « réparer ».

### Espaces et ponctuation haute (fr-FR)
| Signe | Avant | Note |
|---|---|---|
| `:` | insécable U+00A0 | exception : heures numériques (13:52), URL, ratios |
| `;` `!` `?` | fine U+202F (à défaut U+00A0) | `?!` : espace avant le premier signe seulement |
| `,` `.` | rien | — |

fr-CA (OQLF) : insécable avant `:` seulement ; PAS d'espace avant `; ! ?`. « Bonjour! » n'est pas une faute au Québec ; « Bonjour ! » n'en est pas une en France. On ne convertit jamais l'un vers l'autre.

### Majuscules accentuées — tous registres
« L'accent a pleine valeur orthographique » (Académie française). Corriger partout, y compris casual : Etat → État, A noter → À noter, Ca → Ça, EVENEMENT → ÉVÉNEMENT. Exceptions : sigles (CEE), graphies officielles sans accent, identifiants techniques, code.

### Apostrophe
Typographique ’ (U+2019) en académique/professionnel. Exigence minimale partout : COHÉRENCE — jamais de mélange ’/' dans un même texte (l'incohérence est d'ailleurs un signal IA). Jamais ’ → ' (dégradation). Jamais toucher au code.

### Tirets
- L'incise « mot — incise — suite » (espaces autour) est du français CORRECT mais rare. Le tic IA est : le cadratin collé à l'anglaise (`mot—mot`), la cascade d'incises (2-3+ par paragraphe), le cadratin-ponctuation-universelle.
- Correction du tic : reformuler la plupart des incises en virgules ou parenthèses ; si on garde une incise, espaces autour, et l'incise fermée en fin de phrase perd son second tiret.
- Ne JAMAIS : remplacer un tiret d'incise par un trait d'union ; toucher aux tirets de dialogue d'un texte littéraire ; appliquer un « zéro cadratin » dogmatique.
- Intervalles : trait d'union en usage français courant (1914-1918, p. 12-15) ; le demi-cadratin sans espaces (1914–1918) est un usage éditorial admis. Ne convertir NI dans un sens NI dans l'autre.

### Nombres, unités, monnaie
- Milliers : espace insécable (1 234 567) — jamais 1,234,567 ni 1.234.567.
- Décimale : virgule (3,14) — jamais le point en prose. Tous registres (le point décimal change le sens).
- 50 %, 20 °C, 10 km, 14 h 30 : espace insécable. « 50% » collé = calque anglais (toléré en casual).
- Monnaie : symbole APRÈS le nombre (1 500 €, 100 $ CA) — « €1,500 » est un calque à corriger partout.
- Pas de séparateur dans les années (2026), pages, codes postaux.

### Titres — pas de Title Case, tous registres
« Les Meilleures Pratiques De Gestion » → « Les meilleures pratiques de gestion ». Majuscule au premier mot + noms propres. Titres d'œuvres : règle LRTUIN (Les Misérables, À la recherche du temps perdu) et italique ; ne pas décapitaliser un système LRTUIN correct, ne pas « corriger » un système simplifié cohérent — détruire uniquement le Title Case.

### Listes à puces (OQLF)
- Introduites par `:` (avec son insécable).
- Items dépendants de la phrase d'intro : minuscule + `;` final (`,` si très courts), point final au dernier.
- Items phrases complètes : majuscule + point.
- Items très courts (web) : pas de ponctuation, casse cohérente.
- Tous les items de même nature grammaticale (tous infinitifs, tous noms…) — le panachage est une faute IA fréquente.

### Abréviations
M. (jamais Mr), Mme (sans point), Dr, 1ᵉʳ/1ʳᵉ/2ᵉ (jamais 1ère/2ème/2ième), XIXᵉ siècle (jamais 19ème), « , etc. » (jamais etc...), cf., p. ex. plutôt que e.g., c'est-à-dire plutôt que i.e., p. 12 (jamais p12 ni #12), nᵒ 3 (jamais #3). En fin de phrase, le point abréviatif se confond avec le point final.

## Patterns de détection T

Sévérité par registre — A = académique, P = professionnel, L = linkedin, C = casual ; valeurs : **C**orriger / **S**ignaler / **I**gnorer.

| ID | Pattern | Détection | Correction | A | P | L | C |
|---|---|---|---|---|---|---|---|
| T1 | Guillemets non français en 1ᵉʳ niveau | "..." ou “ ” en citation courante | « … » avec insécables | C | C | S | I |
| T2 | Espaces de ponctuation cassées | espace sécable ou absente avant `: ; ! ?` (fr-FR visé) | insécabiliser / ajouter selon variété | C | C | S | I |
| T3 | Majuscules non accentuées | Etat, A ce sujet, Ca, EVENEMENT | accentuer | **C** | **C** | **C** | **C** |
| T4 | Apostrophe droite ou mélangée | ' en registre soigné ; mélange ’/' | ’ partout ; cohérence partout | C | C | S | S |
| T5 | Cadratin à l'anglaise | `mot—mot` collé ; 2+ incises/paragraphe | virgules/parenthèses ; espaces si conservé | C | C | C | S |
| T6 | Virgule d'Oxford | « A, B, et C » en énumération simple | « A, B et C » | C | C | C | S |
| T7 | Title Case | 3+ mots capitalisés dont mots-outils | capitalisation française | **C** | **C** | **C** | **C** |
| T8 | Nombres anglicisés | 3.14, 50%, €1,500, 1,234,567 | 3,14 · 50 % · 1 500 € · 1 234 567 (décimale : tous registres) | C | C | C | S |
| T9 | Abréviations fautives | Mr, 1ère, 2ème, etc..., e.g. | table ci-dessus | **C** | **C** | C | S |
| T10 | Listes mal ponctuées | panachage majuscules/ponctuation | règle OQLF | C | C | S | I |
| T11 | Incohérence typo interne | accents présents puis absents, ’ puis ', « » puis "" | harmoniser vers le niveau le plus soigné présent | C | C | C | S |
| T12 | Points de suspension fautifs | ...., .., . . . | … ou ... cohérent | C | C | C | S |
| T13 | Heures/formats techniques en prose | « rendez-vous à 14:30 » | 14 h 30 | C | C | S | I |

**Exclusions T6** (virgule avant « et » LÉGITIME — ne jamais corriger) : virgule fermant une incise ou une apposition (« Nous avons invité Paul, le directeur, et Marie » — la supprimer changerait le sens) ; virgule de coordination entre propositions à sujets distincts ou pour l'insistance (« Il pleuvait, et la route était glissante » — Grevisse, BDL). Seule l'énumération simple de termes homogènes déclenche.

## Interdictions absolues (rappel — voir aussi SKILL.md)

1. « » → " ou “ ” — le bug fondateur à ne jamais reproduire.
2. ’ → ' ; U+00A0/U+202F → U+0020 ; É → E. Tout pipeline « nettoyage Unicode » naïf est proscrit.
3. Imposer la norme France à un texte québécois ou l'inverse.
4. Tiret d'incise ou de dialogue → trait d'union ; intervalle converti (1914-1918 ↔ 1914–1918).
5. Virgule décimale → point (hors code).
6. Title Case ajouté ; Mr./pp./e.g./# ajoutés lors d'une réécriture.
7. Introduire des « incohérences naturelles » volontaires pour paraître humain : la typographie correcte est un objectif de qualité, jamais un défaut à casser.
8. Toucher à la typographie du code, des URL, des chemins, des littéraux, des citations verbatim.

## Invariant de non-régression (auto-contrôle avant livraison)

Aucune SUBSTITUTION dégradante dans les remplacements effectués : « » → ", ’ → ', insécable → sécable, É → E, virgule décimale → point. En mode fichier, `scripts/audit.py avant.md apres.md` vérifie l'invariant en déterministe (violation = baisse d'un compteur français + hausse de la forme dégradée correspondante).

## Note de composition de ce dépôt

Les fichiers de malherbe sont rédigés en typographie web simplifiée (apostrophes droites, espaces sécables) — registre « chat/code » de la section 10 : c'est du Markdown destiné à GitHub et aux éditeurs de code, où les caractères invisibles sont un piège de maintenance. Exceptions composées AU CARACTÈRE PRÈS : la table Unicode ci-dessus, les paires de règles de ce fichier, et les fixtures SNF-7, SNF-9, SNF-12, SNF-13 et SNF-15 de tests/fixtures.md (textes humains de registre soigné : leur typographie doit être réellement irréprochable à l'octet pour que « Attendu : aucun » tienne face à T2/T4). Les exemples du catalogue illustrent les CARACTÈRES prescrits ; les obligations du skill portent sur le TEXTE TRAITÉ, jamais sur ce dépôt.
