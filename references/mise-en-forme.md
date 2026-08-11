# Famille M — Mise en forme LLM

La signature VISUELLE des sorties IA : gras saupoudré, grilles de puces, émojis structurants, broetry. Selon les analyses 2026 (crackdown LinkedIn), les signaux structurels détectés par les plateformes sont d'abord CEUX-LÀ — avant le lexique.

Principe directeur : **le format n'est pas le crime, le vide l'est.** Une liste est légitime quand le contenu est une liste ; des paragraphes courts sont légitimes sur mobile. On corrige la mécanique et l'uniformité, pas l'usage du format.

Sources : Wikipédia EN (WP:AIBOLD, WP:AILIST, WP:AIEMOJI, WP:AITABLE), Wikipédia FR (★★★ gras/puces/sections calibrées), rapport LinkedIn 2026.

## M1 — Gras mécanique

Mise en gras d'un groupe par phrase, de chaque occurrence d'un terme, ou de mots sans enjeu (« notre **solution innovante** permet de **gérer efficacement** vos **projets** »). Cas FR documenté : résumé NotebookLM avec une expression en gras par phrase. (3 sources.)
Seuil : 3+ groupes en gras par paragraphe, ou gras sur 10 %+ du texte. Correction : garder le gras sur 1-2 concepts réellement clés, ou aucun.
Sévérité : A:C P:C L:C C:S.

## M2 — Listes à puces « **Titre :** description »

Chaque puce ouverte par un mini-titre en gras + deux-points + phrase calibrée : « - **Rapidité :** notre outil est 2× plus rapide. » Répété 3-5 fois, items de longueur identique. LE signe structurel le plus fréquent toutes plateformes. (WP:AILIST + 2 sources.)
Correction : refondre en prose quand la liste n'apporte rien ; sinon liste simple, items INÉGAUX, ordonnés par importance, ponctuation OQLF (voir typographie.md).
**Avant** : « - **Performance :** le site est rapide. - **Sécurité :** tout est chiffré. - **Simplicité :** facile à maintenir. »
**Après** : « Le site charge en moins d'une seconde et chiffre tout de bout en bout. Je le maintiens seul, en quelques minutes par mois. »
Sévérité : A:C P:C (sauf doc produit où la liste est idiomatique — items inégaux alors) L:C C:S.

## M3 — Sur-structuration

Tout le propos en puces là où la prose est attendue ; sections courtes calibrées (1-3 paragraphes homogènes) ; titres de sections interrogatifs en série ; sauts de niveaux de titres (`#` → `###`) ; séparateurs `---` avant chaque titre ; petits tableaux inutiles (« Récapitulatif » de 3 lignes évidentes). (Wikipédia FR ★★★ + WP.)
Sévérité : A:C P:S L:S C:S.

## M4 — Émojis structurants

Émoji-puces uniformes (✅✅✅, 👉👉), émoji-titres (« 🎯 Objectif : », « ⚠️ Le piège : »), 👇 de renvoi, 🚀/✨/💡 décoratifs. (3 sources ; « l'émoji fusée » est devenu le mème du post ChatGPT.)
Correction : 0 par défaut ; 1-2 émojis SIGNIFIANTS (ton, autodérision) tolérés en linkedin/casual. Jamais en grille.
Sévérité : A:C P:C L:S (0-2 signifiants OK) C:I.

## M5 — Broetry

Une phrase (ou un fragment) par ligne sur tout le post, sauts de ligne dramatiques, fragments interrogatifs (« Résultat ? », « La vérité ? », « Mon erreur ? »), lignes d'un seul mot (« Rien. »), escaliers anaphoriques (« Pas de budget. Pas d'équipe. Pas de réseau. »), lignes pivot (« Puis j'ai compris. », « Jusqu'au jour où. »). Format par défaut de l'IA quand on demande « un post LinkedIn » — et pénalisé algorithmiquement depuis 2026.
Détection : ratio paragraphes/phrases ≈ 1 sur plus de 6 lignes ; ≥ 2 fragments dramatiques.
Correction : regrouper en paragraphes de 1-3 phrases (lisibilité mobile CONSERVÉE — ne jamais produire un pavé) ; garder au plus 2-3 respirations si vraie chute.
**Avant** :
« J'ai lancé ma boîte il y a 3 ans.\n\nSans budget.\n\nSans réseau.\n\nRésultat ?\n\n3 millions de CA. »
**Après** :
« Quand j'ai lancé ma boîte il y a trois ans, je n'avais ni budget ni réseau. On a fini l'an dernier à 3 M€ de CA — et l'explication est moins sexy qu'un secret : on a prospecté et livré toutes les semaines, y compris les mauvaises. »
Sévérité : A:C P:C L:C (en cascade) / I (2-3 respirations) C:S.

## M6 — Hooks template et CTA génériques (LinkedIn)

Détail complet dans registres.md (section LinkedIn). Rappel des marqueurs :
- Hooks : « Et si je vous disais que » · « Personne n'en parle, pourtant » · « J'ai fait X pendant Y jours. Voici… » · « Impopulaire mais » · « [X] est mort. » · « Lisez jusqu'au bout » · « Thread 🧵 ».
- CTA LinkedIn : « Et vous, qu'en pensez-vous ? » · « Partagez en commentaire » · « Suivez-moi pour plus » · « Taguez quelqu'un » · « Commentez "GUIDE" » · « Repost si ça peut aider ♻️ » · PS promotionnel.
- CTA pro génériques (pages web, plaquettes) : « N'hésitez pas à nous contacter » · « Contactez-nous dès aujourd'hui » · « Prêt à … ? » · « Demandez une démo » (sans objet concret) · « Faites le premier pas ».
Signal fiable : un CTA ajouté alors que le texte source n'en avait pas = signature IA.
Sévérité : A:C P:C L:C C:S. Exclusion : un CTA spécifique et situé (« Demandez un devis : la simulation prend deux minutes ») reste légitime en professionnel — c'est le générique qui déclenche.

## M7 — Casse de titre anglaise (Title Case)

« Les Meilleures Pratiques Pour Réussir Votre Transformation » — quasi impossible chez un rédacteur FR natif : signe TRÈS fort (plus discriminant en FR qu'en EN). Inclut la sur-capitalisation en cours de phrase (« l'Intelligence Artificielle », « le Marketing Digital »).
Correction : capitalisation française (majuscule au premier mot + noms propres) — règles complètes dans typographie.md (T7).
Sévérité : **C dans les quatre registres.**

## M8 — Profils et pages « en conserve »

Structure type des bios générées : « Qui suis-je ? / Mes passions / Me contacter », émojis + gras + listes, ton CV-chatbot. (WP 10.4 adapté.)
Sévérité : A:— P:C L:C C:S.

## Règle de la famille

Avant de dé-formater, vérifier le SUPPORT de destination : un README, une doc produit, une note interne Notion sont des contextes où puces et gras sont idiomatiques — le tic y est l'uniformité (items calibrés, gras mécanique), pas le format. Un post LinkedIn garde ses paragraphes courts. Un mémoire n'a NI puces dans le développement NI gras d'emphase (la prose rédigée est la norme académique).
