# Étalonnage sur corpus réel — méthodologie et résultats

Réalisé le 2026-08-12 (v1.3.0 → v1.4.0). Objectif : mesurer le skill sur des textes à vérité terrain qu'il n'a JAMAIS vus — le selftest interne valide la cohérence (le skill contre ses propres fixtures) ; cet étalonnage mesure la justesse externe.

## Corpus (14 textes, aveuglés)

**8 textes IA (vérité : slop)** :
- 4 cas positifs des fixtures d'ultimate-humanizer (MIT, auteur tiers) — en excluant explicitement ceux qui avaient inspiré nos propres fixtures (contamination) ;
- le gabarit « biographie publicitaire » documenté comme sortie IA réelle par la communauté Wikipédia FR ;
- 3 générations NAÏVES fraîches (agents à qui l'on a demandé simplement « écris un post LinkedIn / une page À propos / une intro de mémoire », sans un mot sur le style — le comportement par défaut d'un modèle 2026 est l'objet mesuré).

**6 textes humains (vérité : humain, PROUVABLE)** :
- 2 extraits de Wikipédia FR en révisions de 2019, horodatage `oldid` vérifiable (Château de Chambord, oldid 159237381 ; Photosynthèse, oldid 158737493) ;
- 2 billets de blog personnels datés (Zythom, 22/11/2019 ; blog de cuisine, 22/02/2015) ;
- 1 texte institutionnel (Académie française, « Le covid 19 ou la covid 19 », 07/05/2020) ;
- 1 essai du domaine public (Alain, « Bucéphale », 08/12/1922).

**Aveuglement** : les agents de mesure ont reçu des copies SANS les en-têtes de provenance (identifiants neutres T01-T14, lots entrelacés), chaque texte traité comme une demande indépendante, registre imposé par le manifeste. Les extraits sous droits (blogs, Académie) ne sont pas redistribués dans ce dépôt ; leurs URL et dates figurent ci-dessus pour reproduction.

## Protocole

1. **Couche déterministe** : compteurs de `scripts/audit.py` sur chaque texte (en-têtes retirés) → distributions humain vs slop par compteur.
2. **Couche catalogue** : 4 agents chargent le skill installé et traitent chacun un lot en `--dry-run`, en appliquant seuils, exclusions et matrice à la lettre. Verdict par texte : rien / refus de statuer / retouche ciblée / traitement complet.
3. **Constance** : 5 agents identiques et indépendants traitent le même panel de 4 textes (2 slop, 2 humains) → stabilité des verdicts, similarité de Jaccard des ensembles de patterns, taux de clignotement par pattern.

## Résultats

### Détection : 14/14 verdicts corrects

| Vérité | Verdict attendu | Obtenu |
|---|---|---|
| 8 slop | traitement complet | **8/8** |
| 6 humains | rien (0 correction proposée) | **6/6** — zéro faux positif |

Le cas le plus instructif : **T14, l'introduction de mémoire générée naïvement en 2026, marque ZÉRO sur tous les compteurs lexicaux déterministes** (aucun « crucial », aucune cheville, aucun calque) — le slop de génération actuelle a assaini son vocabulaire. Le catalogue l'a détecté quand même : triades calibrées (S3 ×3), évitement de copule (S1 ×2), ouverture générique (R3). **La couche structurelle attrape ce que le lexique ne voit plus** — c'est la validation empirique de l'architecture à 8 familles.

À l'inverse, les agents ont correctement PROTÉGÉ dans le même texte : l'annonce de plan, le lexique méthodologique (problématique, revue de littérature), la triade d'attaque à référents concrets — les conventions académiques ont tenu en conditions réelles.

### Couche déterministe : deux signaux calibrés

- **Densité Tier 2 (adjectifs emphatiques /1000 mots)** : humains = 0,0 sur les 6 textes (max 0,0) ; slop = 9,4 en moyenne. Aucun faux positif possible au seuil actuel — confirmé.
- **Étalement des longueurs de phrases (max − min)** : humains de 35 à 80 ; slop de 4 à 33 à longueur comparable. **Le discriminant le plus robuste du corpus**, et le seul qui survive à l'assainissement lexical des modèles récents → intégré à S13 comme critère quantitatif (étalement < 15 mots sur un texte de 150+ mots = signal moyen).

### Constance (5 passes indépendantes, panel de 4 textes)

- **Verdicts : 100 % stables** — y compris sur les deux textes humains pièges (blog personnel, prose institutionnelle « plate »).
- **Nombre de corrections : stable à ±1.**
- **Ensembles de patterns : Jaccard moyen 0,60 à 0,81** selon le texte. Les patterns « qui clignotent » diagnostiqués et corrigés en v1.4.0 :
  - F7/F11/F12 tantôt comptés comme patterns, tantôt comme signalements → règle explicite ajoutée (ce sont TOUJOURS des signalements) ;
  - « enjeu capital » attribué tantôt F1, tantôt S1+L1b → règle de non-cumul ajoutée ;
  - « explore en profondeur » reconnu par approximation de « exploration approfondie » → ajouté littéralement au Tier 1 ;
  - « exceptionnel/époustouflant/remarquable » classés L6 par principe sans y figurer → ajoutés littéralement à L6.
- **Défense en profondeur vérifiée** : C2 (virgule d'Oxford) a clignoté 2 passes sur 5 sur un texte humain — la règle du faisceau (« un signe faible isolé ne déclenche rien ») a maintenu le verdict « rien » à chaque fois. Le filet fonctionne même quand un pattern individuel hésite.

### Couverture externe du catalogue

27 patterns distincts ont tiré sur le corpus (A3, A10, C1, C5, F1, F2, F7, L1, L1b, L6, M1, M4, M6, R1, R3, R4, R7, R8, R9, R11, R12, S1, S2, S3, S5, S10, S14) — tous à bon escient. Les patterns non exercés par ce corpus (artefacts techniques, typographie cassée, broetry en cascade…) restent validés par les fixtures internes uniquement : ce corpus ne contenait pas leurs déclencheurs. **Aucune suppression décidée sur cette base** — un corpus de 14 textes ne condamne pas un pattern, il départage ceux qu'il exerce.

## Décisions prises (v1.4.0)

1. S13 : critère quantitatif d'étalement calibré sur les données.
2. F7/F11/F12 : statut « signalement, jamais pattern compté » explicité.
3. F1 : non-cumul « enjeu majeur/capital » (F1, pas L1b sur le même segment).
4. L1 Tier 1 : + « explore en profondeur ».
5. L6 : + « exceptionnel(le) », « époustouflant(e) », « remarquable » (contexte promotionnel).

## Limites (à lire avant de citer ces chiffres)

- **n = 14.** C'est un étalonnage, pas une validation statistique. Les 100 % sont encourageants, pas définitifs.
- **Les générations naïves viennent d'un seul modèle** (celui qui exécute) ; les 5 autres textes slop viennent d'auteurs et d'outils tiers, mais la distribution multi-modèles 2026 n'est que partiellement représentée.
- **Le skill est exécuté par un LLM** : les scores mesurent instructions × modèle exécutant. La constance des verdicts (100 %) est la meilleure nouvelle de ce point de vue.
- Les textes humains pré-2022 prouvent l'humanité, pas la représentativité de toute l'écriture humaine actuelle.
- Auto-évaluation du projet, protocole aveuglé mais pas un audit tiers. Tout est reproductible avec les provenances ci-dessus.
