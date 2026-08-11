# Changelog — malherbe

## 1.0.0 — 2026-08-11

Première version.

- 84 patterns en 8 familles (A artefacts, L lexique, C calques, S syntaxe, R remplissage, F fond, M mise en forme, T typographie), chacun avec marqueurs littéraux, seuils, exclusions, avant/après et sévérité par registre.
- Matrice de registres : académique / professionnel / linkedin / casual — sévérité C/S/I par pattern, whitelists (conventions académiques, liste blanche LinkedIn, oralité casual).
- Typographie française normative (LRTUIN, OQLF, Académie) avec invariant de non-régression ; distinction fr-FR / fr-CA / fr-CH.
- Harnais : 2 passes à arrêt dur, seuil de déclenchement en faisceau, gate final à compteurs écrits, ancres sémantiques, anti-« même soupe », garde anti-sur-édition, workflow chat / fichier / non-interactif.
- Règles d'intégrité : anti-fabrication (placeholders « à compléter par l'auteur »), anti-anti-détection, typographie jamais dégradée, anti-injection.
- Benchmark apparié SF/SNF (12 cas SF, dont un cas d'injection de prompt, + 10 SNF) avec protocole --selftest et règle de croissance appariée.
- `scripts/audit.py` : compteurs déterministes (stdlib) + vérification de l'invariant typographique.
