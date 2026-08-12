# Changelog — malherbe

## 1.4.0 — 2026-08-12

Version d'étalonnage : le skill a été mesuré en aveugle sur un corpus externe à vérité terrain (8 textes IA jamais vus — dont 3 générations naïves de 2026 — et 6 textes humains à antériorité PROUVABLE : révisions Wikipédia 2019 via oldid, blogs datés 2015-2019, Académie française 2020, essai de 1922). Résultats : **14/14 verdicts corrects, zéro faux positif, verdicts 100 % stables sur 5 passes indépendantes**. Méthodologie, chiffres et limites : docs/etalonnage.md.

- **S13 renforcé d'un critère quantitatif calibré** : étalement des longueurs de phrases < 15 mots sur 150+ mots = signal moyen (humains du corpus : 35-80 ; IA : 4-33). C'est le discriminant qui survit à l'assainissement lexical des modèles récents — le slop académique 2026 du corpus ne contenait plus AUCUN marqueur lexical et a été détecté par la structure seule.
- **Constance améliorée** (patterns « clignotants » diagnostiqués sur 5 passes) : F7/F11/F12 explicitement définis comme signalements (jamais comptés en patterns) ; non-cumul « enjeu majeur/capital » = F1 ; « explore en profondeur » ajouté au Tier 1 ; « exceptionnel/époustouflant/remarquable » ajoutés à L6.
- Couverture externe documentée : 27 patterns exercés à bon escient par le corpus ; aucune suppression (un corpus de 14 textes départage, il ne condamne pas).

## 1.3.0 — 2026-08-12

- **`--chapitre` (et détection automatique des longs documents)** : traitement section par section avec structure gelée (titres, annonces de plan, transitions, conclusions partielles), seuils appliqués par section, vérifications globales (cohérence terminologique, je/nous, lissage F11), rapport consolidé, validation chapitre par chapitre en mode fichier.
- **`--niveau leger|moyen|agressif`** : l'ampleur d'intervention, orthogonale au registre (le registre décide quoi, le niveau combien) — les protections, whitelists et la règle anti-fabrication ne bougent à aucun niveau.
- **`--diff`** : sortie limitée aux segments modifiés.
- **Glossaire métier** : `.malherbe.md` accueille un glossaire de domaine (jamais corrigé, jamais varié, jamais compté) — modèles commentés avec exemple finance/éco dans `docs/config-projet.md`.
- **Calibration de voix renforcée** : échantillon recommandé de 3-5 pages, profil à 7 dimensions mesurées (dont taux de nominalisation et manière de citer), sections « tics protégés » / « à surveiller » dans `malherbe-voix.md`.
- **Hedging académique** : test de départage en 3 questions dans registres.md — dans le doute, s'abstenir.
- **Citations et références verrouillées plus explicitement** : une citation contenant des tics IA reste verbatim ; une référence ne s'« améliore » jamais, même mal formatée (signalement seulement).
- **Fixtures** : SF-FIN (mémoire de finance slopé, lexique de domaine protégé), SNF-14 (notes humaines maladroites — la maladresse n'est pas un tic IA), SNF-15 (citation à tics verbatim + référence mal formatée signalée, jamais corrigée). Benchmark : 17 SF + 15 SNF.
- **--learn étendu** : journal opt-in des corrections acceptées/refusées en mode fichier — un pattern souvent refusé devient candidat à l'assouplissement.

## 1.2.1 — 2026-08-11

- **Aller-retour PDF documenté** : PDF en entrée → texte corrigé → régénération d'un PDF en sortie via les outils de la session (skill pdf, pandoc), avec avertissement explicite que la mise en page sera standard. La correction de la source (.md, .docx, .tex) reste le chemin recommandé — seul à préserver la mise en page. L'édition d'un PDF en place reste exclue (réalité du format, pas une limite du skill).

## 1.2.0 — 2026-08-11

- **`--aide`** (aussi « malherbe help ») : le skill affiche son mode d'emploi — usage, modes, registres, fichiers de config, garanties — sans traiter de texte.
- **Comportement PDF explicite** : un PDF est lu (jamais édité) ; la version corrigée sort en conversation ou dans un .md à côté, et le skill propose de corriger la source éditable (.md, .docx, .tex) quand elle existe.

## 1.1.0 — 2026-08-11

- **Boucle de complétion interactive** : les placeholders « (à compléter par l'auteur : …) » deviennent des questions posées directement à l'utilisateur (3 max, groupées), intégrées dans une version finale — en session interactive uniquement.
- **Profils persistants** (opt-in, jamais écrits sans accord) : `malherbe-voix.md` (voix calibrée mémorisée) et `.malherbe.md` (registre par défaut du projet, lexique métier whitelisté), auto-chargés à l'étape 0.
- **docs/benchmark.md** : publication du banc d'essai en aveugle contre boileau et ultimate-humanizer (protocole, scores, citations des juges, limites) — classement malherbe premier chez les deux juges ; zéro fabrication et zéro perte d'attribution silencieuse (seul à cumuler les deux).
- **standalone/malherbe-standalone.md** : version condensée monofichier pour tout assistant (ChatGPT, Gemini…).
- **Fixtures étendues** : 4 nouveaux cas SF (tourisme slopé, blog mécanique, fiction pseudo-littéraire, document recopié du chat) et 3 pièges SNF appariés (discours à anaphore réelle, tourisme humain, copie d'étudiant) — 17 patterns supplémentaires couverts (A5-A6, A9, L6, L8, C3, S8-S9, S11, S13-S14, R2, R4-R6, F8, T12). Le benchmark passe à 16 cas SF + 13 SNF.
- **CI et gouvernance** : `scripts/verifie.py` (intégrité déterministe : IDs, décompte, invariants à l'octet, régressions), GitHub Action, templates d'issues faux-positif/pattern, CONTRIBUTING.md (croissance appariée, cadence de révision du lexique, refus de l'anti-détection).
- Corrections de l'audit final : comptage de l'exemple canonique de voix.md (13-12-6), apostrophes typographiques dans SNF-7/SNF-9, harmonisation émojis casual.

## 1.0.0 — 2026-08-11

Première version.

- 84 patterns en 8 familles (A artefacts, L lexique, C calques, S syntaxe, R remplissage, F fond, M mise en forme, T typographie), chacun avec marqueurs littéraux, seuils, exclusions, avant/après et sévérité par registre.
- Matrice de registres : académique / professionnel / linkedin / casual — sévérité C/S/I par pattern, whitelists (conventions académiques, liste blanche LinkedIn, oralité casual).
- Typographie française normative (LRTUIN, OQLF, Académie) avec invariant de non-régression ; distinction fr-FR / fr-CA / fr-CH.
- Harnais : 2 passes à arrêt dur, seuil de déclenchement en faisceau, gate final à compteurs écrits, ancres sémantiques, anti-« même soupe », garde anti-sur-édition, workflow chat / fichier / non-interactif.
- Règles d'intégrité : anti-fabrication (placeholders « à compléter par l'auteur »), anti-anti-détection, typographie jamais dégradée, anti-injection.
- Benchmark apparié SF/SNF (12 cas SF, dont un cas d'injection de prompt, + 10 SNF) avec protocole --selftest et règle de croissance appariée.
- `scripts/audit.py` : compteurs déterministes (stdlib) + vérification de l'invariant typographique.
