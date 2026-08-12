# Banc d'essai en aveugle — malherbe vs boileau vs ultimate-humanizer

Réalisé le 2026-08-11, avant la première publication de malherbe. Objectif : mesurer, pas affirmer. Les trois outils sont exécutés fidèlement (chacun selon son propre SKILL.md) sur trois textes identiques, puis jugés en aveugle par deux évaluateurs indépendants qui ignorent quelle sortie vient de quel outil.

## Protocole

- **Outils** : malherbe v1.0.0 · [alxbd/boileau](https://github.com/alxbd/boileau) (commit 5b272a7) · [surdijon/ultimate-humanizer](https://github.com/surdijon/ultimate-humanizer) v0.3.0. Chaque outil est exécuté par un agent (même modèle, mêmes réglages) qui charge le skill et le suit à la lettre — le skill décide, pas l'agent.
- **Textes** (neufs, hors fixtures de malherbe — reproduits en annexe) :
  1. introduction de rapport de stage slopée — piège : l'annonce de plan, la problématique et le « nous » sont des conventions académiques à préserver ;
  2. post LinkedIn template (hook « Et si je vous disais que », statistique non sourcée « 89 % », broetry, émojis, CTA d'engagement) — piège : les vrais chiffres de l'auteur (12 → 25 rendez-vous) doivent survivre ;
  3. e-mail professionnel authentiquement humain — piège : la seule bonne réponse est de ne PAS le réécrire.
- **Jugement** : 2 juges indépendants (angle 1 : fidélité/intégrité ; angle 2 : français/registre), sorties anonymisées A/B/C, 5 critères sur 10 (fidélité, registre, typographie, déslopification, naturel). Clé d'anonymisation révélée après notation : A = ultimate-humanizer, B = malherbe, C = boileau.

## Résultats

### Classement — identique chez les deux juges : **malherbe > ultimate-humanizer > boileau**

| Totaux /150 | malherbe | ultimate-humanizer | boileau |
|---|---|---|---|
| Juge fidélité | **135** | 127 | 126 |
| Juge français/registre | **133** | 131,5 | 125 |

### Détail par texte (juge fidélité)

| Texte | Critère décisif | malherbe | ultimate-humanizer | boileau |
|---|---|---|---|---|
| 1 — académique | fidélité | **10** | 7 | 3 |
| 1 — académique | déslopification | 6 | 9 | **10** |
| 2 — LinkedIn | déslopification | **10** | 4 | 9 |
| 2 — LinkedIn | fidélité | **9** | 9 | 2 |
| 3 — humain (piège) | total /50 | 49 | 48 | **50** |

## Ce que le banc d'essai a montré

**boileau écrit le plus beau français — et fabrique.** Sur le texte 2, il a inventé une anecdote vécue complète au nom de l'auteur (« Le plus dur : le premier mois. Les chiffres n'avaient pas bougé et on a failli revenir à l'ancien process ») et l'a revendiquée comme méthode (« Ajouté […] une aspérité vécue »). Sur le texte 1 : « séquences d'e-mails, scoring de leads » (outils inventés), « Leurs éditeurs promettent » (attribution inventée). Verdicts des deux juges indépendants — juge fidélité : « *le meilleur styliste et le pire falsificateur* » ; juge registre : « *le post sonne humain parce qu'il ment* ». Fidélité : 2/10 et 3/10.

**ultimate-humanizer est fidèle mais timide.** Aucune fabrication, mais sur le texte 2 l'engagement bait survit tel quel (« Partagez en commentaire, et suivez-moi pour plus de conseils sales »), la statistique non sourcée « 89 % » reste en accroche, et l'aphorisme subsiste aplati. Déslopification : 4/10. Sur le texte 1, « des études montrent » est supprimé silencieusement — l'affirmation devient un fait non sourcé, risqué devant un jury.

**malherbe : zéro fabrication ET zéro perte silencieuse.** Deux outils sur trois n'ont rien fabriqué (malherbe et ultimate-humanizer) ; malherbe est le seul à cumuler l'absence de fabrication ET le traitement honnête de l'attribution vague académique (« Des études montrent [référence requise : Auteur, année] » — là où ultimate-humanizer supprime l'attribution en silence, fidélité 7/10 contre 10/10). Meilleure déslopification du post LinkedIn (10/10) en conservant tous les chiffres réels de l'auteur ; refus argumenté de toucher au texte humain.

**Sa limite, mesurée aussi** : sur le texte académique, l'intégrité a un prix — la sortie contient des placeholders « (à compléter par l'auteur : …) » et reste volontairement sous-nettoyée en attendant les sources (déslopification 6/10 et 5,5/10 selon le juge). C'est un choix de conception (l'alternative observée chez les concurrents : affirmer sans source, ou inventer) — et depuis la v1.1.0, la boucle de complétion interactive transforme ces placeholders en questions posées directement à l'auteur.

**Le texte-piège humain** : les trois outils l'ont réussi — refus de réécrire chez les trois ; la seule restitution intégrale du texte (celle de boileau) a été vérifiée au mot près. C'est le plancher du métier ; les trois le tiennent.

## Vérifications internes (même session)

- **Selftest SF** : 76/76 patterns attendus détectés sur les 12 cas « doit corriger » (rappel 100 %), précision 77/77.
- **Selftest SNF** : 0 faux positif sur les 10 cas pièges « ne doit pas toucher ».
- **Injection de prompt** : instruction embarquée dans le texte traitée comme donnée, jamais exécutée.

## Limites de ce banc d'essai

- n = 3 textes, 2 juges : probant, pas une évaluation massive. Les écarts de 1-2 points ne sont pas significatifs ; les écarts de fidélité (10 vs 2-3) le sont.
- Les trois outils sont exécutés par le même modèle : les scores mesurent la qualité des INSTRUCTIONS de chaque skill, pas une garantie indépendante du modèle.
- Le jugement par LLM, même en aveugle et croisé, n'est pas un jury humain. Les fabrications relevées ont toutefois été vérifiées par citation mot à mot contre les originaux.
- ce banc d'essai est une auto-évaluation du projet, pas l'audit d'un tiers ; le protocole (exécution fidèle de chaque skill, anonymisation, juges sans accès aux skills) est conçu pour neutraliser ce biais, pas pour le faire disparaître. Reproduisez-le : tout est en annexe.

## Annexe — les trois textes originaux

### Texte 1 — introduction de rapport de stage

> Dans un monde en constante évolution, la digitalisation de la fonction commerciale joue un rôle crucial dans la compétitivité des PME. Il convient de noter que les outils de prospection automatisée constituent un enjeu majeur, stratégique et incontournable. Des études montrent que l'enrichissement de données permet d'optimiser les campagnes, de favoriser la personnalisation et de garantir un meilleur taux de réponse, soulignant l'importance fondamentale de la donnée dans le paysage commercial actuel. Ce rapport s'attachera à analyser la problématique suivante : dans quelle mesure l'automatisation du sourcing transforme-t-elle le métier de commercial en PME ? Nous mobilisons pour cela une observation participante de six mois au sein d'une startup. La première partie présente le contexte de l'entreprise ; la deuxième décrit le dispositif de prospection mis en place ; la troisième discute les résultats obtenus, dans la limite de ce terrain unique.

### Texte 2 — post LinkedIn

> Et si je vous disais que 89 % des commerciaux perdent 2 heures par jour sur des tâches sans valeur ?
>
> Personne n'en parle.
>
> Pourtant, c'est LA raison pour laquelle vos équipes n'atteignent pas leurs objectifs.
>
> Il y a 6 mois, j'ai testé un nouveau process.
>
> Résultat ?
>
> Notre équipe de 3 commerciaux a doublé son volume de rendez-vous, en passant de 12 à 25 rendez-vous par mois.
>
> ✅ Automatisez le sourcing
> ✅ Personnalisez chaque message
> ✅ Mesurez tout
>
> La prospection, ce n'est pas une question d'outils. C'est une question de méthode.
>
> Et vous, combien de temps vos équipes perdent-elles chaque semaine ? Partagez en commentaire 👇 Et suivez-moi pour plus de conseils sales 🚀

### Texte 3 — e-mail humain (piège)

> Bonjour Claire,
>
> Merci pour ton retour sur la maquette, ça m'a bien aidé. J'ai repris les trois écrans : le tableau de bord, la fiche client et l'export. Pour l'export, j'ai un doute sur le format — Excel plaît aux commerciaux, mais le CSV passe mieux dans leurs outils. J'ai mis les deux, on tranchera jeudi.
>
> Petit point d'attention : la DA veut le logo en haut à gauche, or sur mobile ça mange la moitié de l'écran. Franchement, je préférerais qu'on le réduise, quitte à froisser un peu le brief. Enfin, on en parle jeudi.
>
> À plus,
> Thomas
