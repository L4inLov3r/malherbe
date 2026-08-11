<div align="center">

# malherbe

**Un skill d'humanisation construit POUR le français, pas traduit de l'anglais.**
Détecte et corrige les marques d'écriture IA — sans dénaturer un texte humain, sans dégrader la typographie française, sans rien inventer.

> « Enfin Malherbe vint. » — Boileau, *L'Art poétique*

![Version](https://img.shields.io/badge/version-1.1.0-2d5f8a?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-2d5f8a?style=flat-square)
![Patterns](https://img.shields.io/badge/patterns-84%20en%208%20familles-2d5f8a?style=flat-square)
![Registres](https://img.shields.io/badge/registres-4-2d5f8a?style=flat-square)

*Français d'abord — English summary at the bottom.*

</div>

---

## Pourquoi malherbe

Les humanizers existants sont pensés pour l'anglais. Appliqués au français, ils détruisent ce qu'ils devraient protéger : l'un convertit les guillemets « français » en guillemets droits, un autre interdit le tiret d'incise, un troisième « améliore » un mémoire en supprimant son annonce de plan — obligatoire dans un mémoire français.

malherbe est construit EN français, POUR le français :

- **84 patterns en 8 familles**, sourcés (Wikipédia FR/EN, OQLF, Académie française, 7 catalogues de praticiens francophones, guides universitaires), chacun avec marqueurs littéraux, seuils, exclusions et exemples avant/après.
- **4 registres** — académique, professionnel, LinkedIn, casual — parce qu'un même marqueur peut être un tic sur LinkedIn et une convention obligatoire dans une thèse. C'est la matrice de registres qui décide, pas une liste de mots interdits.
- **Typographie française normative et jamais dégradée** : guillemets « », espaces insécables, majuscules accentuées (État, À), virgule décimale — avec les différences France/Québec documentées et respectées.
- **Ultra-prudent sur les faux positifs** : seuil de déclenchement en faisceau, patterns faibles qui ne déclenchent jamais seuls, liste des signes d'écriture humaine à préserver, garde anti-sur-édition (« si le passage a un pouls, la bonne édition est souvent : aucune »).

## Testé en aveugle contre ses prédécesseurs

Avant publication, malherbe a été opposé à boileau et ultimate-humanizer sur trois textes neufs (académique, LinkedIn, e-mail humain piège), sorties anonymisées, deux juges indépendants. **Classement identique chez les deux juges : malherbe premier** (135/150 et 133/150) — zéro fabrication ET zéro perte d'attribution silencieuse (seul à cumuler les deux), meilleure déslopification du post LinkedIn. Un des concurrents a inventé une anecdote vécue complète au nom de l'auteur — c'est exactement ce contre quoi malherbe est conçu. Protocole, scores, citations des juges et limites : [docs/benchmark.md](docs/benchmark.md).

## Ce que malherbe refuse de faire

1. **Inventer.** Aucun fait, chiffre, anecdote ou vécu fabriqués pour « faire humain ». Matière manquante → « (à compléter par l'auteur : …) ».
2. **Contourner les détecteurs.** L'objectif est la qualité d'écriture ; aucune fonction anti-détection, aucune erreur volontaire, aucune promesse d'indétectabilité.
3. **Dégrader la typographie.** « » → " est une faute, pas une humanisation.
4. **Réécrire un texte humain.** 0 pattern ou signaux faibles isolés → « Texte déjà humain », point.

## Installation

### Claude Code

```bash
git clone https://github.com/VOTRE_COMPTE/malherbe.git
mkdir -p ~/.claude/skills/malherbe
cp -r malherbe/SKILL.md malherbe/references malherbe/tests malherbe/scripts malherbe/evolution ~/.claude/skills/malherbe/
```

### Autres agents (Codex, Copilot, Gemini CLI, Cursor)

```bash
mkdir -p ~/.agents/skills/malherbe
cp -r malherbe/SKILL.md malherbe/references malherbe/tests malherbe/scripts malherbe/evolution ~/.agents/skills/malherbe/
```

### N'importe quel assistant (ChatGPT, Gemini, Mistral…)

[`standalone/malherbe-standalone.md`](standalone/malherbe-standalone.md) est une version condensée en un seul fichier, à coller dans les instructions personnalisées de n'importe quel assistant. Moins fine que la version complète (pas de fixtures, matrice de registres résumée), mais autonome.

## Usage

```
Humanise ce texte : [texte]
Ce mail sonne trop ChatGPT, corrige-le
/malherbe --registre academique [chapitre de mémoire]
/malherbe --dry-run [texte]            # diagnostic sans réécriture
/malherbe --voice [2-3 § de ton écriture] -- [texte]
/malherbe --explain [texte]            # avant/après détaillé
```

Sur un **fichier**, malherbe liste d'abord ses corrections numérotées et attend ta validation avant d'éditer.

**Boucle de complétion** : quand il manque une source ou un fait (malherbe n'invente jamais), le skill pose directement ses questions (3 max, groupées, en session interactive) et intègre tes réponses — le placeholder est une question, pas une impasse.

**Profils persistants** (opt-in) : `malherbe-voix.md` à la racine de ton projet mémorise ta voix calibrée (fini de recoller l'échantillon --voice) ; `.malherbe.md` fixe le registre par défaut et ton lexique métier whitelisté — les termes de ton domaine que le skill ne « corrigera » jamais.

## Les 8 familles

| Famille | Contenu | Exemple de correction |
|---|---|---|
| **A** Artefacts | oaicite, `utm_source=chatgpt.com`, « J'espère que cela vous aide », placeholders | suppression — preuves quasi certaines |
| **L** Lexique | « joue un rôle crucial », faux soutenu (*effectuer*, *s'avérer*), doublets, jargon corporate | le fait à la place de la proclamation |
| **C** Calques | *adresser un problème*, *faire du sens*, *basé sur*, virgule d'Oxford | retour au français |
| **S** Syntaxe | « Ce n'est pas X, c'est Y », triades, connecteurs en pluie, participes plaqués | affirmer, varier, couper |
| **R** Remplissage | « Il est important de noter que », ouvertures planétaires, conclusions creuses | supprimer la cheville, garder l'assertion |
| **F** Fond | inflation d'importance, « des études montrent » sans source, fausse notoriété | démontrer, sourcer, ou TODO — jamais maquiller |
| **M** Mise en forme | gras mécanique, puces « **Titre :** », émojis structurants, broetry | prose, listes inégales |
| **T** Typographie | « » et insécables, État/À, Title Case, 50 %, fr-FR vs fr-CA | normaliser vers le français, jamais l'inverse |

## Le registre académique, traité sérieusement

Un humanizer naïf détruit un mémoire : l'impersonnel, le passif méthodologique, le hedging épistémique, l'annonce de plan, le « nous » de modestie et la répétition terminologique y sont des **conventions**, pas des tics. malherbe les protège et n'attaque que le vide (emphase non démontrée), le fantôme (« des études montrent » sans référence → TODO bloquant, jamais de réécriture silencieuse) et l'étranger (calques de l'anglais).

## Qualité mesurable

- **Benchmark apparié** : 16 cas « doit corriger » (dont un cas d'injection de prompt) + 13 pièges « ne doit PAS toucher ». Cibles : rappel ≥ 90 %, faux positifs = 0. Protocole : `--selftest`. Dernier run mesuré (v1.0.0, 12+10 cas) : rappel 100 %, faux positifs 0.
- **Gate final à compteurs écrits** : avant de livrer, le skill compte ses propres résidus (y compris les zéros) et liste les longueurs de phrases en chiffres — parce qu'une relecture « de tête » semble toujours propre au modèle qui vient d'écrire.
- **`scripts/audit.py`** : les mêmes compteurs en déterministe (Python stdlib, hors ligne), avec vérification d'invariant typographique (`python3 scripts/audit.py avant.md apres.md` → code retour 1 si la typographie a été dégradée).

## Contribuer

Faux positif ? Pattern manquant ? Les templates d'issues sont prêts, et [CONTRIBUTING.md](CONTRIBUTING.md) décrit les invariants du projet (règle de croissance appariée SF/SNF, cadence de révision du lexique, refus de l'anti-détection). CI : `scripts/verifie.py` (intégrité, y compris à l'octet) + `scripts/audit.py` tournent sur chaque PR.

## Crédits

malherbe fusionne et prolonge deux lignées (MIT, créditées) :
[alxbd/boileau](https://github.com/alxbd/boileau) (le fond linguistique FR) et [surdijon/ultimate-humanizer](https://github.com/surdijon/ultimate-humanizer) (le harnais), eux-mêmes héritiers de [blader/humanizer](https://github.com/blader/humanizer).
Mécaniques inspirées des meilleurs skills d'autres langues : [devswha/patina](https://github.com/devswha/patina), [Raymondhou0917/speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw), [harshaneel/humanize](https://github.com/harshaneel/humanize), [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill).
Sources normatives et communautaires : Wikipédia FR (*Aide:Identifier l'usage d'une IA générative*, Observatoire des IA), Wikipédia EN (*Signs of AI writing*), OQLF (Banque de dépannage linguistique), Académie française, LRTUIN.

---

## English summary

**malherbe** is a French-native Claude Code skill that detects and removes AI-writing patterns from French text. 84 patterns in 8 families, register-aware (academic / professional / LinkedIn / casual — the same marker can be an AI tell in one register and a mandatory convention in another), with normative French typography that is never degraded, strict anti-fabrication rules (missing facts become author TODOs, never inventions), a paired SF/SNF benchmark, and a deterministic audit script. It aims at writing quality, not detector evasion. MIT — credits: boileau, ultimate-humanizer, blader/humanizer.
