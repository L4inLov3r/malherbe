# Contribuer à malherbe

Merci ! Ce dépôt a des règles de maintenance strictes — elles sont ce qui l'empêche de devenir un catalogue de préjugés stylistiques.

## Philosophie : la pertinence, pas les fonctionnalités

Le chemin par défaut doit rester sans friction : coller un texte, dire « humanise ça », c'est tout — aucun flag, aucune config, aucun apprentissage requis. Tout le reste (registres, niveaux, profils) est optionnel et doit le rester.

En conséquence, **les nouvelles fonctionnalités sont refusées par défaut**. Les gains de ce projet viennent de trois sources, et de trois seulement : l'étalonnage sur corpus réel (docs/etalonnage.md), les faux positifs signalés et corrigés, la fraîcheur du lexique (révision par génération de modèles). Une PR qui ajoute un mode, un flag ou une option devra démontrer qu'aucun de ces trois leviers ne pouvait produire le même gain — la charge de la preuve est de son côté. Un outil de détection vaut par sa justesse, pas par sa surface.

## Les invariants (non négociables)

1. **Un pattern = des marqueurs littéraux, des seuils, des exclusions, des sources.** Pas de « ça sonne IA » : des mots exacts, une condition de déclenchement, ce qui ne déclenche PAS, et au moins deux sources indépendantes (ou un corpus).
2. **Règle de croissance appariée.** Tout nouveau pattern ajoute dans `tests/fixtures.md` UN cas SF qui le contient ET UN cas SNF voisin qui ne doit pas déclencher. Un faux positif confirmé devient un cas SNF et la règle reçoit une exclusion — on n'affaiblit jamais un SNF pour sauver une règle.
3. **La typographie française ne se dégrade jamais**, ni dans le skill ni dans ses exemples. `scripts/verifie.py` contrôle les invariants à l'octet.
4. **Aucune fonctionnalité anti-détection.** Les PR qui visent le contournement de détecteurs (erreurs volontaires, métriques de perplexité, « indétectabilité ») seront fermées. C'est un choix de projet, pas un oubli.
5. **FR-natif.** Pas de généralisation multilingue : la force du projet est d'être construit pour le français. Les forks pour d'autres langues sont bienvenus (MIT).
6. **Les exemples « Après » n'inventent rien.** Un exemple modèle qui fabrique un chiffre ou un vécu enseigne la fabrication — c'est le défaut le plus grave possible ici. En cas de matière manquante : « (à compléter par l'auteur : …) ».

## Avant d'ouvrir une PR

```bash
python3 scripts/verifie.py          # intégrité du dépôt (doit sortir 0)
python3 scripts/audit.py tests/fixtures.md
```

Et pour les changements de catalogue : faire tourner le `--selftest` (avec un agent, idéalement un modèle différent de celui qui a rédigé la PR — l'auto-notation gonfle les scores) et rapporter rappel/précision SF et faux positifs SNF dans la description de la PR. Cibles : SF ≥ 90 %, SNF = 0.

## Cadence de révision du lexique

Le vocabulaire IA change à chaque génération de modèles (« delve » est mort en 2025 ; les tics de GPT-4 ne sont pas ceux des modèles 2026). Le Tier 1/Tier 2 de `references/lexique.md` est daté 2025-2026 et se révise par trimestre : les marqueurs qui ne se vérifient plus en corpus passent dans `evolution/proposals.md` (section « À déprécier ») avant retrait.

## Où vivent les choses

- Un pattern vit à UN endroit (sa famille) ; les autres fichiers y renvoient. Pas de duplication.
- Les seuils de registre de `references/registres.md` priment sur les seuils génériques des familles.
- `evolution/` n'est modifié que par le mode opt-in `--learn` et par les mainteneurs — jamais automatiquement.
