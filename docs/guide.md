# Guide d'utilisation — tout ce qu'il faut savoir

Le mode d'emploi complet de malherbe, du premier lancement aux réglages fins. Pour l'installation, voir le [README](../README.md) ; pour les modèles de config, [config-projet.md](config-projet.md).

## Ce que fait malherbe (et ce qu'il refuse)

malherbe détecte et corrige les marques d'écriture IA dans un texte français, selon le registre. Trois garanties structurent tout le reste :

1. **Il n'invente jamais.** Fait manquant → placeholder « (à compléter par l'auteur : …) » puis question directe. Un placeholder est une question, pas une impasse.
2. **Il ne dégrade jamais la typographie française.** Il normalise vers « », les insécables, les majuscules accentuées — jamais l'inverse, et jamais d'une norme (France) vers l'autre (Québec).
3. **Il ne réécrit pas un texte déjà humain.** S'il dit « texte déjà humain, rien à corriger », c'est le comportement attendu — pas une panne.

Et trois refus définitifs : contourner les détecteurs d'IA, faire une troisième passe (la sur-édition tue la voix), remplir lui-même un placeholder.

## Démarrage (5 minutes, une fois par projet)

1. Ouvre une **nouvelle session** de ton agent dans le dossier où tu écris (les skills se chargent au démarrage).
2. **Crée `.malherbe.md`** à la racine : registre par défaut, variété (fr-FR/fr-CA), niveau, et surtout ton **glossaire métier** — les termes de ton domaine que le skill ne corrigera jamais, ne « variera » jamais, ne comptera jamais comme tics. Dis simplement : « crée-moi un .malherbe.md, registre académique, avec ce glossaire : … ». Modèle commenté : [config-projet.md](config-projet.md).
3. **Calibre ta voix** : `--voice` + 3 à 5 pages de TA prose (du même genre que ce que tu vas traiter). Le skill mesure ton profil (longueurs de phrases, nominalisation, connecteurs, manière de citer, tics) et propose de le sauver dans `malherbe-voix.md`. Ensuite, il te connaît à chaque session.

## Les trois gestes du quotidien

| Situation | Geste | Ce qui se passe |
|---|---|---|
| Texte collé | « humanise ça », « ça sonne ChatGPT » | Traitement direct : Lecture (1 ligne) → texte réécrit → Changements → questions éventuelles |
| Fichier | `/malherbe fichier.md` | Liste numérotée des corrections proposées, **STOP**, tu valides (« tout », « 1 à 4 sauf 3 »), il applique |
| Diagnostic seul | `--dry-run` ou `--diff` | Rapport sans réécriture, ou seulement les segments modifiés |

## Tous les modes

| Mode | Usage |
|---|---|
| `--full` (défaut) | Catalogue complet, matrice de registre |
| `--lite` | Passe rapide : patterns cœur seulement |
| `--dry-run` | Diagnostic numéroté, zéro réécriture |
| `--diff` | Seulement les segments modifiés (`- avant` / `+ après`) |
| `--explain` | Avant/après détaillé par pattern (5 max) |
| `--raw` | Le texte seul, sans changelog |
| `--registre academique\|professionnel\|linkedin\|casual` | Force le registre (sinon auto-détecté et annoncé) |
| `--niveau leger\|moyen\|agressif` | Ampleur d'intervention — voir plus bas |
| `--chapitre` | Long document : section par section (auto au-delà de ~1 500 mots) |
| `--voice` + échantillon | Calibration de voix (3-5 pages recommandées) |
| `--learn` | Journal opt-in : tournures hors catalogue + corrections acceptées/refusées |
| `--selftest` | Fait tourner le benchmark interne (17 SF + 15 SNF) |
| `--aide` | Ce guide, en résumé, dans la session |

## Les registres — ce que chacun change

C'est LE réglage qui compte : un même marqueur peut être un tic dans un registre et une convention obligatoire dans un autre.

- **académique** (mémoire, thèse, article) — PROTÈGE l'annonce de plan, les tournures impersonnelles, le passif méthodologique, le « nous », le hedging épistémique, le lexique méthodologique (« problématique », « corpus », « mobiliser »…), la répétition des termes techniques. CORRIGE l'emphase non démontrée, les triades creuses, les calques. « Des études montrent » sans source → **TODO référence, jamais de réécriture silencieuse**.
- **professionnel** (site, doc, e-mail client) — sobriété factuelle : chaque phrase doit porter un fait, un chiffre ou une action. Typographie exigée. Le jargon corporate tombe au-delà d'un terme par paragraphe.
- **linkedin** — le FORMAT est légitime (paragraphes courts, accroche, 0-2 émojis signifiants, question finale sincère) ; le VIDE est le tic (hooks template, stats inventées, broetry mécanique, morale universelle, « partagez en commentaire »).
- **casual** (messages, notes) — préserve ton oralité (« du coup », « bref », « c'est pas »), tes fragments, ta typographie telle quelle. Ne corrige que le pire + l'orthographe (accents sur majuscules, dus partout).

## Les niveaux — combien corriger

- **leger** : les corrections certaines seulement (artefacts, typo, calques, formules Tier 1). Idéal en dernier coup d'œil avant envoi.
- **moyen** (défaut) : la matrice du registre telle quelle.
- **agressif** : corrige plus fort (les signalements deviennent des corrections, seuils abaissés) — mais jamais autre chose : protections, glossaire, zones gelées et anti-fabrication sont invariants. À réserver aux textes très slopés.

Le registre décide QUOI, le niveau décide COMBIEN.

## Workflow type : le mémoire

1. **Rédige d'abord, humanise ensuite** — chapitre par chapitre au fil de l'eau, jamais le document entier la veille du rendu.
2. `.malherbe.md` avec registre académique + ton glossaire (voir l'exemple finance de config-projet.md).
3. `/malherbe --chapitre chap2.md` → il traite section par section, structure gelée (titres, annonce de plan, transitions intouchables), et te fait valider chapitre par chapitre.
4. **Réponds à ses TODO** : chaque « [référence requise : Auteur, année] » est un point faible devant le jury — donne la source ou coupe l'affirmation.
5. Le PDF est l'export FINAL. malherbe lit les PDF mais ne les modifie jamais : on corrige la source (.md, .docx), on exporte à la fin.

## Workflow type : le post LinkedIn

Colle ton brouillon, c'est tout. Il garde ton format et tes vrais chiffres, tue les hooks template et l'engagement bait, et si le nettoyage vide le post… il te demandera la matière réelle au lieu de réhabiller du vide.

## Les cinq règles du bon usage

1. **« Déjà humain » = croire.** Insister pour une réécriture dégrade un texte qui a une voix.
2. **Deux passes maximum.** Il refusera la troisième — c'est voulu.
3. **Du vrai dans les placeholders.** Il te demande un chiffre parce que l'alternative serait de l'inventer. Donne du réel, ou dis « coupe ».
4. **Valide vraiment les listes** en mode fichier (au lieu de « tout » systématique). Avec `--learn`, tes refus lui apprennent où il est trop zélé.
5. **Sois précis sur le contexte** quand l'auto-détection peut se tromper : « c'est un rapport de stage » vaut mieux qu'un registre deviné.

## Dépannage express

| Symptôme | Réponse |
|---|---|
| Il a « corrigé » un terme de mon domaine | Ajoute-le au glossaire de `.malherbe.md` — et si tu penses que c'est un défaut du catalogue, issue « faux positif » sur le repo |
| Il touche à mes tournures personnelles | Calibre ta voix (`--voice`) et mets-les en « tics protégés » dans `malherbe-voix.md` |
| Trop timide / trop de retouches | `--niveau agressif` / `--niveau leger` |
| Je veux voir sans qu'il touche | `--dry-run`, ou `--diff` pour la vue compacte |
| Je lui donne un PDF | Il le lit et corrige à côté (.md) ou régénère un PDF neuf — jamais d'édition du PDF en place |
| Le skill ne se déclenche pas | Nouvelle session (chargement au démarrage), ou appelle-le par son nom : `/malherbe` |
| Mise à jour du skill | `git pull` dans le repo puis recopie vers `~/.claude/skills/malherbe/` (mêmes dossiers que l'installation) |

## Aller plus loin

- [config-projet.md](config-projet.md) — les modèles `.malherbe.md` et `malherbe-voix.md` commentés, avec un glossaire finance/éco d'exemple.
- [benchmark.md](benchmark.md) — le banc d'essai en aveugle contre boileau et ultimate-humanizer, protocole et scores.
- [../standalone/malherbe-standalone.md](../standalone/malherbe-standalone.md) — la version monofichier pour ChatGPT, Gemini et compagnie.
- [../CONTRIBUTING.md](../CONTRIBUTING.md) — proposer un pattern, signaler un faux positif, les invariants du projet.
