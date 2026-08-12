# Famille S — Syntaxe et structure de phrase

Les constructions mécaniques qui trahissent la génération, indépendamment du vocabulaire. C'est la famille où le RISQUE DE FAUX POSITIF est le plus élevé : la rhétorique française légitime (triade classique, anaphore à la de Gaulle, variation élégante scolaire) ressemble à plusieurs de ces tics. Toujours raisonner en faisceau et vérifier les exclusions.

Sources : Wikipédia EN (WP:AIPARALLEL, WP:RO3, WP:AIELEVAR — verdicts de transposabilité), catalogues praticiens FR (comptes de consensus), boileau, guides universitaires.

## S1 — Évitement de la copule (« est »/« sont »/« a »)

L'IA remplace les verbes simples par des périphrases pompeuses : constitue · représente · incarne · se présente comme · s'affirme comme · s'impose comme · se positionne comme · fait office de · fait figure de · sert de · demeure · se révèle être · se distingue par · se caractérise par · dispose de · bénéficie de · désigne / fait référence à (en ouverture de définition). Mesuré : −10 % de « is/are » dans l'écriture académique dès 2023, et le phénomène se voit en FR.
Détection : 2+ périphrases de copule dans un paragraphe, ou 3+ par page. Exclusion : chaque verbe est correct isolément ; « constitue » a des emplois juridiques précis.
**Avant** : « Cette méthode constitue une référence du domaine. Elle représente un standard et s'impose comme l'outil incontournable des équipes. »
**Après** : « Cette méthode est largement utilisée : trois équipes sur quatre l'ont adoptée depuis 2024. »
Sévérité : A:S P:C L:C C:S. (Signal fort, adapté WP:AISEUDO + boileau.)

## S2 — Contrastes binaires et parallélismes en miroir

LE tic rhétorique IA par excellence (3 sources + WP:AIPARALLEL « tel-quel »). Variantes à détecter :
« Ce n'est pas X, c'est Y » · « Ce n'est pas seulement/qu'un X, c'est Y » · « Non seulement X, mais aussi/encore Y » · « Il ne s'agit pas de X, mais de Y » · « La question n'est pas X, c'est Y » · « Le vrai sujet n'est pas X » · « X ne consiste pas à A, mais à B » · « Loin d'être X, c'est Y » · « Moins X, plus Y » · « X ne suffit pas, il faut Y » · « Pas de A, pas de B. Juste C. » (négation en rafale) · « X n'est pas une fatalité, c'est une opportunité » · « Cessons de voir X comme A, voyons-le comme B » · « On pourrait croire X, mais la vérité c'est Y » · « X est souvent perçu comme A, mais en réalité B » · « X plutôt que Y » (forme Grok) · « davantage A que B ».
Le problème : la structure définit ce que la chose N'EST PAS au lieu d'affirmer. Correction : garder l'affirmation, couper le préambule négatif.
Détection : 1 = signal moyen ; 2+ par page = fort. Exclusion : un contraste UNIQUE réellement porté par les faits (« contrairement à la v1, la v2 chiffre les données ») est une comparaison légitime, pas un tic.
**Avant** : « Ce n'est pas un simple outil de gestion, c'est un partenaire stratégique. Non seulement il optimise vos flux, mais il transforme aussi votre culture. »
**Après** : « L'outil gère les flux de commandes. Depuis son déploiement, les équipes priorisent leurs sprints autrement. »
Sévérité : A:C P:C L:C C:S.

## S3 — Règle de trois systématique

Triades d'adjectifs (« simple, rapide et efficace »), de groupes, d'exemples — partout, avec des items calibrés à la même longueur, souvent closes par « et autres X ». (2 sources + WP:RO3.)
Détection : 2+ triades par page dont les éléments ne sont pas repris ensuite (test de reprise). EXCLUSIONS MAJEURES : (1) ne comptent JAMAIS les énumérations de référents CONCRETS (objets, ingrédients, gestes, dates, détails sensoriels), même multiples — le tic est la triade d'ABSTRACTIONS calibrées (adjectifs d'éloge, bénéfices, concepts interchangeables), pas la liste de choses réelles d'une recette ou d'un récit ; (2) la rhétorique ternaire est culturellement valorisée en français (tradition classique) — une triade isolée, même abstraite, reste normale. Ne jamais corriger seul. Nuance : dans un texte déjà en TRAITEMENT COMPLET (faisceau dense), une triade abstraite unique se rapporte « sous seuil — compte en faisceau » ; l'exclusion (2) protège les textes sains, pas les cas déjà déclenchés.
**Avant** : « Notre plateforme est rapide, fiable et sécurisée. Elle s'adresse aux particuliers, aux entreprises et aux institutions. »
**Après** : « Notre plateforme répond en moins de 200 ms. Deux cents entreprises l'utilisent depuis le lancement. »
Sévérité : A:C P:C L:C C:S (toujours en faisceau).

## S4 — Connecteurs en pluie

« Par ailleurs, », « De plus, », « En outre, », « En effet, », « Ainsi, », « Par conséquent, », « De ce fait, », « En somme, », « Dès lors, » en tête de phrases consécutives. L'IA française connecte BEAUCOUP plus que l'IA anglaise. (5 sources — 2ᵉ marqueur le plus cité.)
Détection (seuils du registre courant ; académique plus tolérant, voir registres.md) : > 40 % des phrases d'un paragraphe ouvertes par un connecteur = suspect ; > 70 % = certain ; même connecteur 3+/page = suspect.
Exclusion : la densité de connecteurs est LÉGITIME en académique (un connecteur toutes les 2-4 phrases, plus aux articulations) — le tic est la mécanique (chaque phrase, même connecteur, « En effet » qui n'explique rien, « Ainsi » qui ne conclut rien).
**Avant** : « Le marché évolue. Par ailleurs, les attentes changent. De plus, la concurrence se renforce. En outre, les règles se durcissent. »
**Après** : « Le marché évolue vite : attentes, concurrence, réglementation. »
Sévérité : A:S P:C L:C C:S.

## S5 — Participes présents analytiques plaqués

Une proposition en « -ant » accrochée en fin de phrase pour simuler la profondeur : « …, soulignant » · « témoignant de » · « illustrant » · « reflétant » · « garantissant » · « offrant ainsi » · « permettant de » · « favorisant » · « contribuant à » · « renforçant » · « ouvrant la voie à » · « s'inscrivant dans ». Structure transposée telle quelle de l'anglais (WP:SUPERFICIAL) et massive en FR. (2 sources.)
Détection : 2+ par page. Correction : supprimer la participiale (elle n'ajoute presque jamais un fait) ou en faire une phrase autonome SOURCÉE.
**Avant** : « Le musée a attiré 50 000 visiteurs, témoignant de l'intérêt croissant pour l'art contemporain et s'inscrivant dans la dynamique culturelle régionale. »
**Après** : « Le musée a attiré 50 000 visiteurs — 20 % de plus que l'objectif, selon sa directrice. »
Sévérité : A:C P:C L:C C:C.

## S6 — Anaphores rythmées marketing

« Pour celles qui… Pour celles qui… Pour celles qui… » · « Parce que… Parce que… » · « Quand… Quand… » · « Plus de X. Plus de Y. Plus de Z. » — répétition d'attaque pour un effet « inspirant ». (3 sources.)
Exclusion : l'anaphore assumée d'un discours réel OU d'une prose narrative/littéraire dont la répétition porte des référents concrets est un choix d'auteur — ne jamais la compter. S6 ne vise que l'anaphore marketing à bénéfices abstraits, et seulement en faisceau.
**Avant** : « Pour celles qui osent. Pour celles qui inventent. Pour celles qui ne renoncent jamais. »
**Après** : « Pour les femmes qui veulent essayer autre chose, sans complexe. »
Sévérité : A:C P:C L:C C:S.

## S7 — Nominalisations en chaîne

« La mise en œuvre de l'optimisation de la gestion de la relation client » — l'empilement de noms d'action sans verbe porteur. (Cataloguée par les praticiens ; ATTENTION : la nominalisation est le mode NORMAL de la prose académique et administrative.)
Détection : 3+ nominalisations enchaînées dans un même segment, dans un registre non académique. Correction : re-verbaliser.
**Avant** : « La mise en place de l'amélioration des processus de traitement des demandes est en cours. »
**Après** : « Nous améliorons le traitement des demandes. »
Sévérité : A:**I** P:C L:C C:C.

## S8 — Passif impersonnel qui masque l'acteur

« Il a été décidé de » · « Des efforts ont été déployés » · « Des mesures ont été prises » — le passif qui escamote QUI agit. (2 sources.)
Exclusion capitale : le passif MÉTHODOLOGIQUE académique (« les données ont été collectées par questionnaire ») est standard et protégé ; le passif administratif est naturel ; le passif technique de documentation logicielle (« l'exception est levée », « la valeur est retournée ») est standard et protégé. Le tic est le passif qui masque une responsabilité qui compte.
**Avant** : « Il a été décidé de restructurer le service. Des efforts ont été déployés pour accompagner les équipes. »
**Après** : « La direction a restructuré le service. Deux personnes accompagnent les équipes depuis mars. »
Sévérité : A:**I** P:C L:C C:S.

## S9 — Variation élégante (synonymie compulsive)

Le même référent désigné par une chaîne de synonymes : « le protagoniste… le personnage principal… le héros… notre homme ». Pénalité de répétition du modèle. (WP:AIELEVAR + 1 source.)
EXCLUSION MAXIMALE : l'école française enseigne explicitement la chasse aux répétitions — c'est LE faux positif le plus probable de tout le catalogue en FR. Ne compter qu'en faisceau, jamais corriger agressivement chez un humain. En académique : ne JAMAIS « varier » un terme technique (protégé).
Détection : 3+ désignations différentes du même référent en un paragraphe, quand la reprise du mot serait plus claire.
**Avant** : « Le serveur héberge le site. La machine sert les pages. Le nœud délivre le contenu. »
**Après** : « Le serveur héberge le site et sert les pages. »
Sévérité : A:S (jamais sur les termes techniques) P:S L:S C:I.

## S10 — Fausses gammes (« de X à Y »)

« De la startup à la multinationale » · « de la stratégie à l'exécution, en passant par la gouvernance » · « qu'il s'agisse de X ou de Y » — deux extrêmes pour simuler l'exhaustivité, sans échelle réelle. (boileau + 1.)
**Avant** : « De la PME au grand groupe, notre méthode s'adapte à tous les contextes. »
**Après** : « Notre méthode est utilisée par des entreprises de 10 à 5 000 salariés. »
Sévérité : A:C P:C L:C C:S.

## S11 — Structure dissertation mécanique

« Dans un premier temps… Dans un second temps… Enfin… » recyclé partout, y compris hors dissertation ; « Premièrement/Deuxièmement/Troisièmement » à chaque section. (2 sources.)
Exclusion : en académique, l'annonce de plan est OBLIGATOIRE (registres.md) ; le tic est le squelette mécanique répété à chaque échelle, pas l'annonce elle-même. La correction académique est une annonce FLUIDIFIÉE, jamais supprimée.
Sévérité : A:S (fluidifier) P:C L:C C:C.

## S12 — Hedging empilé

« Il pourrait potentiellement être possible que… puisse peut-être » — 3+ modalisateurs sur une phrase qui n'affirme rien. (2 sources.)
Exclusion : le hedging ÉPISTÉMIQUE académique porte sur une affirmation précise et est une compétence (« ces résultats suggèrent, sans que la causalité puisse être établie ») — protégé. Le tic est le flou généralisé sans objet.
**Avant** : « Il est possible que certains facteurs puissent éventuellement, dans une certaine mesure, jouer un rôle. »
**Après** : « L'ancienneté du parc machine peut jouer. On manque de données pour trancher. »
Sévérité : A:I (épistémique) / C (flou sans objet) P:C L:C C:S.

## S13 — Uniformité de longueur (burstiness faible)

3+ phrases consécutives de longueur quasi identique (± 3 mots) ; texte entier dans la bande 18-22 mots ; paragraphes tous calibrés. (3 sources + mesures.)
Critère quantitatif calibré sur corpus (étalonnage 2026-08, docs/etalonnage.md) : sur un texte de 150+ mots, un étalement des longueurs de phrases (max − min) INFÉRIEUR à 15 mots est un signal moyen — les textes humains du corpus s'étalent de 35 à 80, les textes IA de 4 à 33 à longueur comparable. C'est le marqueur qui survit quand le lexique IA d'une nouvelle génération de modèles s'est assaini.
Correction : casser par une phrase courte (≤ 8 mots) ou fusionner ; viser un étalement max−min ≥ 15 mots par page. NE PAS fabriquer de contenu pour allonger : on redistribue l'existant.
Sévérité : A:S P:C L:C C:S.

## S14 — Questions rhétoriques en cascade

« Et si la solution était là, sous nos yeux ? Et si nous regardions au mauvais endroit ? » · « Comment expliquer ce phénomène ? C'est ce que nous allons voir. » (setup rhétorique). Une question rhétorique isolée est admise (surtout en SHS) ; la cascade est un tic.
Détection : 2+ questions rhétoriques consécutives, ou question + « c'est ce que nous allons voir ».
Sévérité : A:C P:C L:C C:S.
