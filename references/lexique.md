# Famille L — Lexique

Vocabulaire sur-représenté dans les sorties IA françaises. Sources : consensus de 7 catalogues praticiens FR (le compte de sources est indiqué par pattern), Wikipédia EN « Signs of AI writing » (WP:AIVOCAB, adapté — liste FR native, pas traduite), boileau, guides universitaires.

## Les quatre lois de la famille L

1. **Lecture littérale.** Un mot sur-employé par l'IA n'implique RIEN sur ses synonymes. La liste se lit mot à mot, pas par champ sémantique.
2. **Tiers de confiance.** Tier 1 : suspect dès la première occurrence. Tier 2 : suspect en densité (2+ dans un paragraphe, 3+ par page). Tier 3 : jamais suspect seul — ne compte qu'en faisceau avec d'autres familles.
3. **Catalogue daté.** Le lexique IA change à chaque génération de modèles (« delve » est mort en 2025 ; GPT-5 sur-emploie d'autres mots que GPT-4). Ce catalogue est calibré 2025-2026 et doit être révisé — voir evolution/.
4. **Whitelist par registre.** En académique, le lexique méthodologique (problématique, mobiliser, articuler, corpus, dispositif, significatif…) ne compte JAMAIS — voir registres.md.

## L1 — Vocabulaire IA à tiers de confiance

**Tier 1 — suspect dès 1 occurrence** (formules quasi exclusives des sorties IA) :
« dans un monde en constante évolution » · « dans le paysage [adjectif] en constante évolution » · « à l'ère du numérique / de l'IA / du digital » (en ouverture) · « plongeons dans » / « plongez dans » · « exploration approfondie » · « joue un rôle crucial » · « marque un tournant majeur/décisif » · « témoigne de l'engagement » · « empreinte indélébile » · « un véritable levier de croissance » · « tirer parti de tout le potentiel » / « libérer le potentiel »

**Tier 2 (alias L1b) — suspects en densité (2+/paragraphe ou 3+/page)** :
crucial · essentiel · fondamental · incontournable · primordial · majeur · central · clé (adjectif) · stratégique · pivotal · significatif (hors statistique) · captivant · fascinant · passionnant · passionné(e) · engagé(e) (valeurs) · transformateur · révolutionnaire · disruptif · robuste · innovant · dynamique · vibrant · pérenne · durable (figuré) · précieux (figuré) · sur mesure · expertise (pointue) · savoir-faire (isolé, non qualifié) · souligner / mettre en lumière / mettre en évidence / mettre en avant (en cascade) · témoigner de · refléter · incarner · favoriser · renforcer · enrichir · valoriser · optimiser · sublimer · réinventer · donner vie à · paysage (abstrait) · écosystème (abstrait) · mosaïque (figuré) · méticuleux(-sement) · subtilités · interaction (pour « interplay ») · s'aligner avec/sur · en phase avec · fluide (marketing)

Quand un rapport cite la densité Tier 2, l'identifiant est **L1b** (SKILL.md, fixtures, audit.py l'utilisent).

**Tier 3 — jamais seuls** (mots normaux, signaux seulement en faisceau) :
important · nécessaire · riche · profond · pertinent · complexe · efficace · notamment · véritablement

Consensus : les adjectifs emphatiques sont LE marqueur le plus cité du corpus FR (6 sources sur 7).

**Correction** : remplacer la proclamation par le fait. « Ce projet joue un rôle crucial dans notre croissance » → « Ce projet représente 30 % de notre chiffre d'affaires 2025 ». Si aucun fait n'est disponible : dégonfler (« intervient dans », « compte pour ») ou poser « (à compléter par l'auteur : quel chiffre/fait concret ?) ». Ne JAMAIS inventer le fait.

Sévérité : A:C P:C L:C C:S (Tier 1) · selon densité (Tier 2).

## L2 — « Véritable » antéposé

« un véritable défi », « une véritable opportunité », « un véritable atout », « une véritable révolution ». Quasi toujours supprimable sans perte. Seuil : 2+ par texte. Exclusion : « véritable » contrastif réellement porteur (« le véritable auteur du rapport est… »).
**Avant** : « Cette fonctionnalité représente un véritable atout pour vos équipes. »
**Après** : « Cette fonctionnalité fait gagner un clic sur chaque commande. »
Sévérité : A:C P:C L:C C:S. (1 source + corpus boileau.)

## L3 — Verbes passe-partout

permettre de (en chaîne) · garantir · assurer · offrir · proposer · favoriser · optimiser · valoriser · accompagner · répondre aux besoins/enjeux · mettre en place · mettre en œuvre · s'inscrire dans (hors académique) · tirer parti de. (4 sources.)
Seuil : 3+ dans un paragraphe, ou 2 « permettre de » dans une phrase. Exclusion : chaque verbe est normal isolément ; « s'inscrire dans une littérature » est du lexique académique légitime.
**Avant** : « Notre solution permet d'optimiser vos processus et de répondre aux besoins des équipes en mettant en place une approche personnalisée. »
**Après** : « Notre outil supprime trois clics par commande. L'équipe logistique gagne une heure par jour. »
Sévérité : A:S P:C L:C C:S.

## L4 — Faux registre soutenu

L'IA confond « bien écrit » et « écrit avec des mots compliqués ». Table de rétrogradation (2 sources + boileau) :

| IA-soutenu | Mot juste |
|---|---|
| effectuer | faire |
| procéder à | faire |
| s'avérer (copule pure) | se révéler, se trouver |
| disposer de | avoir |
| problématique (nom, HORS académique) | problème |
| thématique | sujet, thème |
| finalité | but |
| opportunité (= occasion favorable) | occasion |
| se doter de (en rafale) | adopter, se donner, s'équiper de |
| au final | finalement, au bout du compte |
| solliciter | demander |
| préconiser | conseiller |

Exclusions L4 (le mot juste reste le mot juste) :
- « il s'avère que » ne se rétrograde JAMAIS en « il est que » (agrammatical) — reformuler en « en fait », « vérification faite » si le tic est avéré ; « le test s'est avéré négatif » porte une valeur de découverte que « était négatif » perd : ne corriger que la copule pure sans enjeu de vérification.
- « opportunité » au sens propre (caractère opportun : « juger de l'opportunité d'une intervention ») ne se remplace JAMAIS par « occasion » — contresens.
- « se doter de » est du français standard (« la ville s'est dotée d'un plan climat ») : ne compter qu'en densité avec d'autres marqueurs L4, jamais isolément.
- « initier un projet » est traité en calque (C1), pas ici — pas de double comptage.

Exclusions majeures : en ACADÉMIQUE, « problématique » est le mot juste (sens méthodologique) et une partie de ce registre soutenu est légitime — voir registres.md. Dans un courrier administratif, « solliciter » est normal. Le tic est le soutenu PLAQUÉ sur un contexte qui ne le demande pas.
**Avant** : « Nous avons procédé à l'analyse de la problématique et disposons des éléments pour effectuer les corrections. »
**Après** : « On a analysé le problème ; on a ce qu'il faut pour le corriger. »
Sévérité : A:I P:C L:C C:C.

## L5 — Doublets d'adjectifs quasi synonymes

« simple et intuitif », « robuste et fiable », « innovant et performant », « rapide et efficace », « cohérent et personnalisé », « clair et structuré », « complexe et multiforme », « riche et varié ». Tic statistique : l'IA accole deux adjectifs dont le second n'ajoute rien. (2 sources.)
Seuil : 2+ doublets par page. Exclusion : doublets TECHNIQUES à contenu distinct (« validité interne et externe », « quantitative et qualitative », « fixe et mobile »).
**Avant** : « Une interface simple et intuitive pour une expérience fluide et agréable. »
**Après** : « Une interface prise en main en (à compléter par l'auteur : votre durée mesurée) — chiffre réel, pas promesse. »
Sévérité : A:C P:C L:C C:S.

## L6 — Langage promotionnel et touristique

« niché au cœur de », « au cœur de » (figuré) · « écrin de verdure » · « joyau » · « véritable havre » · « riche patrimoine » · « riche histoire » · « à couper le souffle » · « dépaysement garanti » · « incontournable » · « emblématique » · « de renom » · « se targue de » / « peut s'enorgueillir de » · « offre une expérience unique » · « un large éventail de » · « une gamme variée de » · « charme authentique » · « hors du temps » · « nous croyons en/que » (credo d'entreprise) · « écrire un nouveau chapitre » / « la suite de votre histoire ». Registre brochure ou plaquette d'agence, déclenché dès qu'on parle de lieu, patrimoine, entreprise. (Adapté de WP:AIPUFFERY + boileau.)
**Avant** : « Nichée au cœur de la vallée, cette ville incontournable au riche patrimoine offre une expérience unique. »
**Après** : « La ville compte 8 000 habitants. Son église romane du XIIᵉ siècle est classée depuis 1932. »
Sévérité : A:C P:C L:C C:S.

## L7 — Jargon corporate français

Antérieur à l'IA (langue de bois RH/conseil), mais l'IA le CONCENTRE : le tic est la densité, pas la présence. Seuil : ≥ 3 termes / 4 lignes sans aucun fait concret. (Rapport LinkedIn + 24heures/Taleez.)

| Jargon | Traduction honnête |
|---|---|
| c'est dans notre ADN | dire quoi, concrètement |
| donner du sens | dire à quoi ça sert |
| co-construire | décider ensemble |
| embarquer les équipes | convaincre, associer |
| aligner / on est alignés | d'accord, cohérent |
| faire monter en compétence | former |
| acculturer (les équipes à) | former à, familiariser avec |
| intelligence collective | travail de groupe (ou couper) |
| game changer | dire ce qui change |
| scalabilité / scaler | passer à l'échelle |
| mindset | état d'esprit |
| best practices | bonnes pratiques |
| quick win | gain rapide |
| data-driven | fondé sur les chiffres |
| l'humain au cœur de | supprimer ou prouver par un fait |
| bienveillance / authenticité (en rafale) | max 1, illustrées par un comportement |
| roadmap | feuille de route |
| impulser une dynamique | lancer |
| activer les synergies | (couper) |

**Avant** : « Nous co-construisons avec nos équipes une feuille de route ambitieuse pour donner du sens à notre transformation et embarquer chaque collaborateur. »
**Après** : « On a revu l'organisation avec les équipes : trois ateliers par service, 40 propositions, 12 retenues. Premier changement en septembre. »
Sévérité : A:C P:C L:C C:S.

## L8 — Registre pseudo-littéraire (fiction)

Quand on demande du « littéraire », l'IA produit un registre mièvre identifiable (2 sources, dont une dédiée) : « un instant suspendu » · « comme si le temps s'était figé » · « une promesse murmurée/brisée/silencieuse » · « un secret brûlant » · « un désir vibrant » · « un silence vibrant » · comparaisons en « comme si / comme une » systématiques · noms abstraits + participes émotionnels.
**Avant** : « Il la regarda, comme si le temps s'était figé. Une promesse murmurée, un secret brûlant entre eux. »
**Après** : « Il la regarda. Personne ne parla pendant une bonne minute. »
Sévérité : tous registres C quand le texte est de la fiction ; sans objet ailleurs.

## L9 — Faux registre familier plaqué

« ça pique », « ça coince », « ça envoie », « plus qu'honnête », « fait le job », « plutôt cool » insérés dans un texte par ailleurs pro/analytique. Miroir inverse de L4 : quand on demande à l'IA d'être « naturelle », elle saupoudre des idiomes sur un fond formel. Un humain choisit son registre et s'y tient. (boileau.)
Détection : ≥ 2 idiomes familiers dans un texte majoritairement formel. Exclusion : registre familier assumé de bout en bout (casual) — là, ces marqueurs sont de l'ORALITÉ à préserver.
**Avant** : « L'analyse du Q3 montre une stagnation du taux de conversion. Là où ça pique vraiment, c'est sur le panier moyen. »
**Après** : « Le taux de conversion stagne au Q3. Le vrai problème : le panier moyen, en baisse de 12 %. »
Sévérité : A:C P:C L:S C:I.

## L10 — Mots fétiches en boucle

Le même mot rare revient à fréquence anormale dans un même texte (« promesse » ×6, « vibrant » ×4). Différent de la répétition terminologique légitime (un terme technique répété est normal, surtout en académique). (2 sources.)
Détection : mot non technique répété 4+ fois / 500 mots. → varier ou dégonfler.
Sévérité : A:I P:S L:S C:I.
