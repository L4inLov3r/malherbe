# Configuration projet — `.malherbe.md` et `malherbe-voix.md`

Deux fichiers opt-in, à la racine de ton projet, chargés automatiquement par le skill (étape 0). Aucun des deux n'est jamais créé ni modifié sans ton accord.

## `.malherbe.md` — la config du projet

Fixe le comportement par défaut et — surtout — le **glossaire métier** : les termes de ton domaine que le skill ne corrigera jamais, ne « variera » jamais (S9 désactivé pour eux) et ne comptera jamais comme tics, quel que soit le registre.

```markdown
# Config malherbe — Mémoire M2 finance

registre: academique
variete: fr-FR
niveau: moyen

## Glossaire métier (intouchable : jamais corrigé, jamais varié, jamais compté)

<!-- Adapte cette liste à TON sujet — exemple pour un mémoire de finance : -->
- due diligence
- spread (de crédit)
- carry trade
- asymétrie d'information
- aléa moral
- sélection adverse
- covenant
- levier (financier)
- coût du capital
- MEDAF / CAPM
- actualisation / DCF
- juste valeur
- goodwill
- titrisation
- collatéral
- prime de risque
- taux sans risque
- efficience (semi-forte) des marchés
- value at risk (VaR)
- duration
- mark-to-market
- hors-bilan
- normes IFRS
- EBITDA
- besoin en fonds de roulement (BFR)
- significatif (au sens statistique)

## Tournures maison autorisées

<!-- Les formules de TON document que le skill pourrait prendre pour des tics : -->
- « Ce chapitre montre que » (transitions de chapitre)
- « Nous entendons par X » (définitions liminaires)
```

Notes :
- Les anglicismes du glossaire (due diligence, carry trade, mark-to-market…) sont du **lexique de domaine consacré** — les « franciser » serait une faute professionnelle, pas une humanisation. Le glossaire prime sur la famille C.
- « significatif » près d'un test statistique est déjà protégé par le registre académique ; le lister le rend explicite.

## `malherbe-voix.md` — ton profil de voix

Produit par la calibration `--voice` (échantillon recommandé : 3 à 5 pages de TA prose, du même genre que le texte à traiter). Le skill le propose après calibration ; tu peux aussi le remplir à la main.

```markdown
# Profil de voix — [ton nom / ton projet]
calibré le : 2026-08-12
échantillon : 4 pages (introduction + chapitre 2 du mémoire), ~1 800 mots

## Mesures
- longueur des phrases : moyenne 21 mots, écart-type 9, de 6 à 41
- paragraphes : 3 à 6 phrases
- connecteurs en tête de phrase : ~1 phrase sur 4 (favoris : toutefois, en revanche, dès lors)
- nominalisation : modérée (verbe préféré quand les deux se valent)
- voix : « nous » de modestie, impersonnel en méthodologie ; jamais de « je »
- citations : parenthétiques (Auteur, année) ; citation longue en retrait au-delà de 3 lignes

## Ponctuation
- deux-points fréquents, parenthèses rares, jamais de points de suspension
- tiret d'incise : occasionnel (1-2 par page maximum)

## Tics protégés (c'est MA voix, ne pas « corriger »)
- « Reste que » en attaque de paragraphe
- tendance aux questions de transition en fin de section (1 max)

## À surveiller chez moi (je le sais)
- « en effet » en excès quand je me relis mal
```

La section « Tics protégés » prime sur le catalogue : un marqueur qui y figure n'est jamais corrigé. La section « À surveiller » fait l'inverse : le skill peut y être plus strict que le seuil normal.
