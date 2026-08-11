# Registres — la matrice qui décide de tout

Un même marqueur peut être un tic IA dans un post LinkedIn et une convention obligatoire dans un mémoire. malherbe ne corrige jamais « dans l'absolu » : il corrige PAR RAPPORT À UN REGISTRE. C'est la première décision de tout traitement.

Notation de sévérité utilisée dans toutes les familles : **C** = corriger, **S** = signaler sans corriger, **I** = ignorer, **TODO** = signaler avec placeholder bloquant, jamais de réécriture silencieuse (famille F). Colonnes : A = académique, P = professionnel, L = linkedin, C = casual.

## Détection du registre

Si `--registre` est fourni, l'appliquer. Sinon, auto-détecter et **l'annoncer en tête de réponse** (« Je traite ce texte comme [académique] — dis-moi si c'est faux ») :

| Registre | Indices |
|---|---|
| **académique** | références (Auteur, année), notes de bas de page, bibliographie, « problématique », « corpus », « méthodologie », sections numérotées, « nous » de modestie, hedging épistémique |
| **professionnel** | doc produit, page web d'entreprise, e-mail client, deck, newsletter ; vouvoiement commercial, « notre solution/équipe/offre » |
| **linkedin** | post court, hook en première ligne, hashtags, émojis, lignes courtes, première personne entrepreneuriale |
| **casual** | message perso, Slack, e-mail entre collègues ; tutoiement, oralité, absence de structure |

Ambiguïté réelle (rapport de stage qui ressemble à un deck, newsletter qui ressemble à un post) : choisir le plus PROTECTEUR (celui qui corrige le moins), l'annoncer, et signaler l'hésitation. Cas hors matrice : documentation technique/API → professionnel avec les protections de la doc sèche (passif technique légitime, prose plate normale) ; courrier formel de particulier → professionnel avec les rituels administratifs protégés (anti-faux-positifs §2).

Variété linguistique (fr-FR / fr-CA / fr-CH) : détectée indépendamment du registre — voir typographie.md. On ne convertit jamais une variété vers une autre.

---

## Registre ACADÉMIQUE (mémoire, thèse, rapport de stage, article)

Le registre où un humanizer naïf fait le plus de dégâts : le style académique français est PAR CONVENTION impersonnel, nominal, connecté, prudent et méta-discursif — exactement ce qu'un détecteur calibré sur le web flaggerait à tort.

**Règle d'or : protéger la forme conventionnelle ; n'attaquer que le vide, le fantôme et l'étranger.**
- le **vide** : emphase non démontrée, triades non reprises, chevilles, conclusions universelles ;
- le **fantôme** : attributions sans référence → TODO bloquant, jamais de réécriture silencieuse ;
- l'**étranger** : calques lexicaux et typographiques de l'anglais.

### Protégé — ne PAS corriger (whitelist)

1. **Nominalisations** (« la mise en œuvre de », « la prise en compte de ») : mode normal de la prose scientifique. Ne toucher que l'empilement (> 3 nominalisations enchaînées sans verbe porteur).
2. **Tournures impersonnelles et « on »** (« il ressort de l'analyse que », « on observe ») : marque d'objectivité recommandée par les guides universitaires.
3. **Passif méthodologique** (« les données ont été collectées par questionnaire ») : standard en Méthodologie/Résultats. Critiquable seulement s'il masque une attribution qui compte.
4. **« Nous » de modestie / « je » assumé** : le choix appartient à l'auteur. Ne JAMAIS convertir nous↔je. Détecter seulement l'incohérence (mélange non motivé dans un même chapitre) → signalement.
5. **Connecteurs structurants** : densité légitime d'un connecteur toutes les 2-4 phrases, concentration normale aux articulations. Seule la mécanique est un tic (voir seuils).
6. **Hedging épistémique** (« ces résultats suggèrent », « dans la limite de cet échantillon ») : compétence académique, les copies les mieux notées modalisent. Tic seulement si le flou ne porte sur aucune affirmation identifiable (≥ 3 modalisateurs empilés sur une phrase qui n'affirme rien).
7. **Lexique méthodologique — whitelist stricte** : problématique (nom), mobiliser, articuler, s'inscrire dans (une littérature), appréhender, corpus, dispositif, paradigme, opérationnaliser, triangulation, saturation, revue de littérature, cadre conceptuel, posture épistémologique, biais, limites, validité interne/externe. **« significatif » près d'un test statistique ne se reformule JAMAIS.** Ces termes ne comptent pas dans les scores de jargon.
8. **Répétition terminologique** : en académique on répète le terme exact ; la variation synonymique des termes techniques crée de l'ambiguïté conceptuelle. Désactiver l'anti-répétition.
9. **Méta-discours conventionnel** : l'annonce de plan est OBLIGATOIRE en fin d'introduction ; transitions inter-parties, chapeaux et conclusions partielles (« Ce chapitre a montré que… »), définitions liminaires, rappels de problématique — exigences de genre. Seule amélioration admise (en suggestion) : fluidifier une annonce ultra-mécanique (« Dans une première partie… Dans une deuxième partie… Dans une troisième partie… »), jamais la supprimer.
10. **Zones gelées** : citations directes (au caractère près, y compris leurs éventuels tics), références et normes (APA, ibid., op. cit., et al.), notes de bas de page, bibliographie, annexes, résumé/abstract, légendes, latinismes académiques (a priori, in fine, stricto sensu).
11. **Phrases longues maîtrisées** : seuil d'alerte à ~40-45 mots, pas 25. Formules rituelles (remerciements, avertissements de confidentialité).

### À corriger MÊME en académique

1. **Inflation d'importance** : « joue un rôle crucial », « revêt une importance capitale », « enjeu majeur » en rafale. L'importance se démontre, elle ne se proclame pas. → dégonfler + préciser.
2. **Triades vides** : énumération ternaire dont les éléments ne sont pas repris ensuite. Test de reprise : chaque élément a-t-il une existence propre dans la suite ? → réduire à ce qui est traité.
3. **Doublets creux** : « complexe et multiforme », « claire et précise ». (≠ doublets techniques à contenu distinct : « validité interne et externe », « quantitative et qualitative » — whitelist.)
4. **Attribution vague sans référence — le tic MORTEL** : « des études montrent », « il est largement admis », « il a été démontré que » SANS (Auteur, année) dans la phrase ou la suivante. Proche de la faute méthodologique. → **TODO bloquant** : signaler « référence requise », ne JAMAIS reformuler silencieusement ni inventer une source. Même traitement pour le name-dropping non sourcé (« comme l'a montré Bourdieu » sans année ni œuvre).
5. **Ouvertures grandioses et conclusions génériques** : « Dans un monde en constante évolution… », « domaine prometteur appelé à se développer ». Une conclusion académique rappelle la problématique, synthétise les résultats OBTENUS, énonce limites et ouverture PRÉCISE.
6. **Remplissage** : « il convient de noter que » en rafale (1/page passe), paraphrase du titre en ouverture de section, tautologies, « au niveau de » non spatial. Test de suppression : la phrase supprimée, perd-on quelque chose ?
7. **Sur-connectorisation mécanique** : chaque phrase d'un paragraphe ouverte par un connecteur ; le même connecteur ≥ 4/page ; « En effet » qui n'explique rien ; « Premièrement/Deuxièmement » recyclé à chaque section.
8. **Calques de l'anglais** (les jurys y sont sensibles) : adresser un problème, supporter une hypothèse, évidence(s) pour preuves, digital, impacter, en termes de, versus, au final, être en charge de + tous les calques typographiques (Oxford comma, Title Case, "…").
9. **Contrastes mécaniques** : « Ce n'est pas X, c'est Y », « non seulement… mais aussi » > 1/page, questions rhétoriques en cascade.
10. **Lissage structurel** (diagnostic seulement) : paragraphes tous identiques, chaque section close par une mini-conclusion positive → signalement, la correction relève de l'auteur.

### Seuils (pour ~1 page ≈ 350-400 mots)

| Marqueur | Toléré | Tic certain |
|---|---|---|
| « il convient de / il est important de » | 1/page | ≥ 3/page ou 2 dans le même § |
| emphase (crucial, essentiel, majeur…) | 1/page | ≥ 3/page ou 2 dans la même phrase |
| même connecteur | ≤ 2/page | ≥ 4/page |
| phrases d'un § ouvertes par un connecteur | < 40 % | > 70 % |
| triades sans reprise | 1/page | ≥ 3/page |
| incises à tirets | 0-1/page | ≥ 3/page |
| attribution vague sans référence | **0 — jamais toléré** | dès la 1ʳᵉ occurrence → TODO |
| « non seulement… mais aussi » | 1/2-3 pages | ≥ 2/page |

Tests qualitatifs, dans l'ordre : (1) zone gelée ? (2) whitelist ? (3) l'affirmation est-elle adossée à une référence/donnée ? (4) test de suppression, (5) test de reprise, (6) test de spécificité (la phrase conclurait-elle n'importe quel mémoire ?), puis seulement (7) fréquence/position.

### Sorties à deux niveaux — spécificité académique

- **Corrections auto** : chevilles vides, calques, typographie, doublets creux, inflation.
- **Signalements** (section « À toi de jouer » du changelog) : référence manquante (TODO), incohérence je/nous, lissage structurel, annonce de plan mécanique, passage irrécupérable. En académique, une réécriture silencieuse peut créer une faute pire que le tic (perte de nuance épistémique, terme technique dénaturé).

---

## Registre PROFESSIONNEL (docs produit, pages web, e-mails clients, decks, newsletters)

Le registre Boldo typique. Objectif : sobriété factuelle — chaque phrase porte un fait, un chiffre, une action.

**Exigé** : typographie web soignée (« », U+00A0, apostrophe typographique, accents, 50 %) ; suppression du jargon corporate au-delà d'un terme par paragraphe (ADN de l'entreprise, co-construire, embarquer les équipes, aligner, donner du sens, game changer, scalabilité, mindset, best practices, quick win — traductions dans lexique.md) ; chasse aux doublets, triades, inflation, langage promotionnel.
**Toléré** : « nous » d'entreprise ; un CTA spécifique et situé (« Demandez un devis : la simulation prend deux minutes ») — le contenu promotionnel assumé est honnête, on nettoie sa langue, pas son intention ; structure titres + puces si le support l'exige (doc produit).
**Signalé** : phrase irrécupérable (aucun fait à préserver) → demander la matière réelle plutôt que reformuler du vide ; statistique invérifiable.
**Interdit au skill** : inventer des chiffres, des références clients, des résultats.

---

## Registre LINKEDIN (posts, contenus personnels professionnels)

Principe directeur : **la mise en forme LinkedIn n'est pas un crime, c'est le vide qui en est un.** Depuis 2026, LinkedIn pénalise algorithmiquement le broetry, l'engagement bait et les posts flaggés « AI slop » — nettoyer ces tics est aussi une question de portée.

### Liste blanche — ne PAS corriger
1. Paragraphes courts (1-3 phrases) : 80 % des lectures sont mobiles.
2. Une accroche travaillée en première ligne (le crime est le template, pas l'accroche).
3. 0-2 émojis signifiants (ton, autodérision) ; le tic est la grille d'émojis structurants.
4. Une vraie liste quand le contenu est une liste — la rendre inégale, hiérarchisée.
5. Une question finale sincère et spécifique (pas « Et vous, qu'en pensez-vous ? »).
6. 1-2 sauts de ligne dramatiques s'il y a une vraie chute.
7. Le « je », le vécu, l'anecdote personnelle : c'est le genre du média.
8. 0-3 hashtags sobres en fin de post.
9. Annonces assumées (poste, lancement, événement) : on nettoie la langue, pas l'intention.

### À corriger
1. **Broetry** : cascade 1 phrase = 1 ligne sur > 6 lignes, fragments dramatiques (« Résultat ? », « La vérité ? »), lignes d'un seul mot, escaliers anaphoriques (« Pas de budget. Pas d'équipe. Pas de réseau. »), lignes pivot (« Puis j'ai compris. »). → regrouper en paragraphes de 1-3 phrases, garder au plus 2-3 respirations justifiées.
2. **Hooks template** : « Et si je vous disais que… », « Personne n'en parle, pourtant… », « J'ai fait X pendant Y jours. Voici… », « Impopulaire mais… », « [X] est mort. », « Lisez jusqu'au bout… ». → réécrire le hook à partir de l'information la plus concrète réellement présente dans le post.
3. **Statistiques faussement précises non sourcées** (87 %, 92 %, 47 824 €) : signature IA. → supprimer ou demander la source. Ne jamais en générer.
4. **Storytelling template** : anecdote minuscule → pivot solennel (« Ce jour-là, j'ai compris ») → morale disproportionnée (« En entreprise, c'est exactement pareil ») → CTA. On casse la mécanique apparente, pas le storytelling. Anecdote sans aucun détail spécifique + dialogue trop calibré → **signaler** (« cette anecdote semble générique — c'est du vécu réel ? ») plutôt que polir.
5. **CTA génériques** (« Partagez en commentaire ! », « Suivez-moi pour plus », « Taguez quelqu'un », « Commentez GUIDE ») : engagement bait pénalisé. → supprimer ; un post peut finir sur sa dernière idée forte. Signal fiable : si le texte source n'avait pas de CTA et que la version « améliorée » en a un, c'est l'IA.
6. **Émojis structurants** : émoji-puces uniformes (✅✅✅), 👇, 🚀/✨ décoratifs, émoji-titres (🎯 Objectif :). → 0-2 émojis signifiants au plus, listes en tirets/numéros, items de longueurs variées.
7. **Jargon corporate en densité** : ≥ 3 termes / 4 lignes sans fait concret = signature (IA ou langue de bois — à traiter pareil).
8. **Fins inspirantes creuses** : maximes gnomiques (« Le succès n'est pas une destination… », « La vraie question n'est pas X. C'est Y. ») → couper, finir sur le dernier fait concret.
9. **Fausse vulnérabilité** : aveu-vitrine (« Je ne partage pas souvent ça… » + succès, « J'ai failli refuser une offre à 6 chiffres », rags-to-riches compressé). Signaux : l'aveu ne coûte rien, le creux dure une phrase, la rédemption est immédiate, l'émotion est déclarée jamais montrée. → réécrire vers le mécanisme réel si la matière existe, sinon signaler.
10. **« Fier et honoré », « belle aventure humaine », « avec beaucoup d'émotion »** : calques et rituels RH creux.

### Le test central du registre
Après nettoyage, chaque phrase restante doit contenir un fait, une opinion assumée ou une émotion montrée. **Si le nettoyage vide le post, le problème n'était pas la forme : le dire à l'auteur et demander la matière manquante. Ne jamais régénérer du vide mieux habillé.**

### Assemblage des signaux (déclenchement)
1 signal fort = suspicion, retouches ciblées. 2 signaux forts, ou 1 fort + 2 moyens = traitement complet. Les éléments de la liste blanche ne comptent jamais comme signaux.

---

## Registre CASUAL (messages, e-mails perso, Slack)

Le registre le moins interventionniste. On corrige le pire, on préserve la personne.

**À corriger** : artefacts d'assistant (« J'espère que cela vous aide »), méta-annonces lourdes, inflation ridicule en contexte (« ce déjeuner d'équipe marque un tournant stratégique »), majuscules non accentuées (orthographe due partout), Title Case.
**À préserver absolument** : l'oralité (« du coup », « bref », « franchement », « c'est pas »), les fragments, l'imperfection vivante, la typographie telle quelle (guillemets droits OK, pas d'espace avant `!` OK). Si l'auteur a tapé « », des insécables et des ' : les conserver intégralement.
**Interdit** : formaliser (convertir « c'est pas » → « ce n'est pas »), imposer « », imposer la ponctuation soignée — dégrader l'oralité d'un humain est l'équivalent casual du bug typographique.

---

## Récapitulatif — ce que le mode change

| Comportement | A | P | L | C |
|---|---|---|---|---|
| Chasse au passif / à l'impersonnel | OFF | doux | ON | OFF |
| Chasse au méta-discours | OFF (conventionnel) | ON | ON | doux |
| Chasse au hedging | OFF (épistémique) | ON | ON | doux |
| Anti-répétition terminologique | OFF | doux | ON | ON |
| Typographie | stricte (print) | stricte (web) | tolérante | préservation |
| Attribution vague | TODO bloquant | corriger | corriger | signaler |
| Oralité (« du coup », « bref ») | corriger | signaler | préserver | préserver |
| Longueur de phrase — seuil d'alerte | ~40-45 mots | ~30 | ~25 | libre |
| Émojis | corriger | corriger | 0-2 tolérés | libres |
| Sortie signalements (TODO) | systématique | si vide | si vide/fabriqué | rare |
