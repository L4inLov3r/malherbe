# Voix, rythme, calibration

Retirer les tics ne fait que la moitié du travail : un texte propre mais sans voix sonne IA même sans aucun marqueur. Cette page dit comment redonner du relief — SANS RIEN INVENTER. C'est la page la plus dangereuse du skill : mal appliquée, elle fabrique du faux vécu. La règle anti-fabrication prime sur tout ce qui suit.

## La règle anti-fabrication (absolue)

malherbe ne crée JAMAIS : un fait, un chiffre, une anecdote, une opinion, une émotion, une expérience, une source que l'auteur n'a pas fournis. « Une fausse histoire est pire qu'une phrase creuse : la phrase creuse est ennuyeuse, la fausse histoire est un mensonge. »

Ce que malherbe PEUT faire :
- réorganiser, condenser, rythmer la matière EXISTANTE ;
- transformer une émotion DÉCLARÉE en émotion montrée à partir des seuls éléments présents (« j'étais déçu du lancement » + « douze ventes le premier mois » → « Douze ventes le premier mois. La déception tient dans le chiffre. » — rien d'autre que la matière fournie, réagencée) ;
- poser un placeholder quand la matière manque : « (à compléter par l'auteur : un exemple vécu, un chiffre, une date) » ;
- demander : « ce passage est creux — donne-moi le fait réel et je l'intègre ».

Livrer un texte avec des placeholders n'est pas un échec. Livrer un texte avec du vécu inventé en est un.

## Signes d'un texte sans voix (même « propre »)

- Toutes les phrases de la même longueur ; tous les paragraphes du même gabarit.
- Aucune opinion, aucun parti pris — « d'un côté… de l'autre » sans trancher.
- Aucun doute, aucune nuance vécue, aucune émotion montrée.
- Aucune première personne là où le contexte l'appelle.
- Aucune aspérité : pas d'humour, pas de digression, pas de contre-exemple.
- Lit comme une fiche ou un communiqué. (« Absence de voix » : 5 sources — 4ᵉ marqueur le plus cité.)

## Redonner du rythme (burstiness) — sur la matière existante

1. **La phrase courte de rupture.** Après deux phrases longues, une phrase de ≤ 8 mots. « Résultat : zéro remboursement. » est une phrase valide.
2. **La phrase longue qui déplie.** Une phrase de 30-40 mots qui prend le temps de poser le décor, avec une incise ou une précision, avant d'arriver à l'idée — puis on coupe court.
3. **Paragraphes asymétriques.** Un paragraphe d'une phrase à côté d'un paragraphe de six, c'est un choix, pas un défaut.
4. **Casser les listes calibrées.** Items de longueurs inégales, ordonnés par importance, avec un contre-exemple ou un aveu (« on a laissé tomber le livret d'accueil : personne ne le lisait »).
5. **Varier les attaques.** Question, chiffre, cas concret, contre-idée — jamais deux sections qui démarrent pareil.
6. **Vérification comptable** (gate final, SKILL.md) : écrire la liste des longueurs de phrases en chiffres. Cible indicative : étalement max−min ≥ 15 mots par page, moins de la moitié des phrases dans la bande 10-20 mots. Une relecture mentale « semble toujours variée » au modèle qui l'a écrite ; la liste de nombres ne ment pas.

Interdits : allonger pour faire « riche » (le remplissage réintroduit les patterns retirés) ; fragmenter en drame (R11) ; fabriquer une digression.

## Redonner une voix — sur la matière existante

- **Trancher quand l'auteur tranche.** Si le texte source contient un jugement (« on a préféré X »), le rendre net : « X, sans hésiter » plutôt que « X pourrait être considéré comme préférable ».
- **Assumer l'incertitude réelle.** « Je ne sais pas si ça tiendra à l'échelle » est plus humain que trois modalisateurs empilés — si le doute est dans le texte source.
- **Préserver les aspérités existantes** (anti-faux-positifs.md §3) : sentiments mitigés, incises, imperfections délibérées, oralité de registre.
- **Le « je » quand le genre l'appelle** (LinkedIn, blog perso) — si l'auteur parle déjà en « je ». Ne jamais convertir un « nous » académique en « je » ni l'inverse.
- **Une pointe d'humour ou d'autodérision** : uniquement en réagençant ce que l'auteur a dit (son aveu, son échec raconté) — jamais en inventant le trait.

## Calibration de voix (--voice + échantillon de 2-3 paragraphes)

Distiller l'échantillon en hypothèses TESTABLES, puis contraindre la réécriture :

1. **Longueurs** : moyenne et étalement des phrases de l'échantillon (écrire les chiffres).
2. **Registre** : tutoiement/vouvoiement, niveau de langue, densité de jargon assumé.
3. **Ponctuation** : usage des deux-points, parenthèses, tirets, points de suspension.
4. **Attaques de phrase et transitions** : entre directement ou contextualise ? connecteurs favoris ?
5. **Tics personnels** : mots fétiches, images récurrentes, manière de trancher ou de nuancer, ironie.

Règles :
- Ne pas seulement retirer les patterns IA : les remplacer par les patterns DE L'ÉCHANTILLON.
- Le registre de l'échantillon PRIME sur les préférences du skill en cas de conflit (si l'auteur écrit avec des tirets d'incise, on en garde).
- Les tics personnels de l'auteur qui ressemblent à des tics IA (un auteur qui aime les triades !) sont PROTÉGÉS : c'est sa voix. Les noter dans la Lecture.
- La calibration contraint le STYLE, jamais le fond : aucun contenu nouveau.
- Sans échantillon : viser un français naturel, concret, direct — pas un « style » plaqué.

## Profil de voix persistant (`malherbe-voix.md`)

Après une calibration --voice réussie, PROPOSER à l'utilisateur de sauvegarder le profil distillé dans `malherbe-voix.md` à la racine de son projet — jamais d'écriture sans son accord. Format du fichier : les 5 dimensions ci-dessus en clair (longueurs mesurées, registre, ponctuation, attaques, tics protégés), plus une ligne de date. Aux exécutions suivantes, le skill le charge automatiquement (étape 0) : la voix est calibrée sans recoller d'échantillon. Le profil se met à jour sur demande (« recalibre ma voix ») — jamais silencieusement.

Fichier compagnon `.malherbe.md` (config projet, même logique opt-in) : registre par défaut du projet, variété (fr-FR/fr-CA), lexique maison whitelisté — les termes métier du projet qui ne doivent JAMAIS être comptés comme tics ni « variés ».

## Lecture (une ligne, avant de réécrire)

Annoncer la lecture : « Je lis ceci comme : [type de texte] pour [audience], registre [A/P/L/C], variété [fr-FR/fr-CA] » — et, si --voice : « voix calibrée sur ton échantillon : phrases courtes, tutoiement, ironie sèche ». Ça ancre les choix et permet à l'utilisateur de corriger AVANT la réécriture.

## L'exemple canonique (avant / après / pourquoi)

**Avant (propre mais sans pouls)** :
« L'expérience a produit des résultats intéressants. Les agents ont généré trois millions de lignes de code. Certains développeurs étaient impressionnés, d'autres sceptiques. Les implications restent floues. »

**Après (avec un pouls — même matière, zéro fait ajouté)** :
« Trois millions de lignes de code, générées sans qu'un humain touche au clavier. Une partie des devs applaudit, l'autre explique pourquoi ça ne compte pas. Et les implications, honnêtement, restent floues. »

Ce qui a changé : le rythme (13-12-6 mots, chute courte), l'opposition rendue vivante, le doute assumé en fin. Ce qui n'a PAS changé : les faits (trois millions de lignes, réactions partagées, incertitude). Rien n'a été inventé — « sans qu'un humain touche au clavier » reformule strictement « les agents ont généré » ; « une partie… l'autre » reprend « certains… d'autres » SANS quantifier (écrire « la moitié » aurait été une fabrication) ; l'« honnêtement » porte le « restent floues » déjà présent.
