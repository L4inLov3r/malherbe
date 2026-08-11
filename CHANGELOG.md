# Changelog — malherbe

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
