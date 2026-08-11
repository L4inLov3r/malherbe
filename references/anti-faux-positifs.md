# Anti-faux-positifs — ce que malherbe ne corrige JAMAIS

La moitié du mandat de malherbe est négative : **ne jamais dénaturer un texte humain**. Réécrire du texte humain AJOUTE de l'IA-ité (mesuré). Cette page est lue AVANT toute correction. En cas de doute après l'avoir appliquée : s'abstenir — le texte reste celui de l'auteur.

Sources : Wikipédia EN « Signs of AI writing » (sections « Unreliable signs » et « Signs of human writing »), Wikipédia FR « Aide:Identifier l'usage d'une IA générative » (§ faux positifs), doctrine des meilleurs skills (patina, Aboudjem, speak-human-tw).

## 1. Les huit indices INEFFICACES (ne prouvent rien, ne déclenchent rien)

1. **La grammaire parfaite.** Beaucoup d'humains écrivent très bien. Un texte impeccable n'est pas un texte généré.
2. **Le mélange de registres** (familier + formel, clinique + émotionnel). Typique des techniciens, des jeunes, de la neurodivergence, des textes à plusieurs mains.
3. **La prose « fade » ou « robotique ».** L'IA a des tics SPÉCIFIQUES (ce catalogue) ; « ça sonne plat » n'est pas un critère. Le style administratif est naturellement plat chez l'humain aussi — zone à très haut risque.
4. **Le vocabulaire soutenu ou académique.** La corrélation ne vaut que pour les mots PRÉCIS du catalogue (lecture littérale) — pas pour tout le lexique recherché.
5. **Un connecteur isolé.** Un « De plus » ou un « Cependant » seul ne prouve rien ; les transitions sont normales en rédaction humaine.
6. **L'absence de sources.** Les humains n'en mettent pas toujours ; les LLM modernes en mettent (mal). Ni la présence ni l'absence ne signalent l'IA.
7. **Le balisage étrange.** Vient plus souvent d'un outil (éditeur visuel, extension) que d'un LLM.
8. **La typographie soignée.** Apostrophes courbes, espaces insécables, guillemets « » cohérents = un rédacteur soigneux ou un traitement de texte, PAS une IA. Un concurrent présente la typo parfaite comme un signal à casser : c'est une faute. Le seul marqueur typographique valide est le MÉLANGE incohérent (T11).

## 2. Situations à présomption d'humanité

- **Chronologie** : texte antérieur à novembre 2022 = humain (2021 : très probablement ; 2018 : certainement). Vérifier l'historique quand il existe (git, versions de docs).
- **Traduction automatique** : un texte traduit présente des défauts proches des LLM (lissage, calques). Un texte « lissé » peut être une traduction d'un original humain — demander avant de traiter.
- **Contributeur inexpérimenté** : mise en page maladroite, références mal formées, majuscules erratiques ne prouvent rien.
- **Texte standardisé** : notes de service, courriers administratifs, documentation sèche — plats par nature et par convention.
- **Contrainte de rédaction** : un humain non natif, pressé, ou écrivant sous gabarit (fiche produit, formulaire) coche mécaniquement des cases du catalogue.

## 3. Signes d'écriture HUMAINE — à préserver activement

Constructions empiriquement PLUS fréquentes chez les humains que dans les sorties IA. Règle absolue : ne jamais les « améliorer » — ce sont des signatures d'humanité.

- **Les copules et tournures simples** : « il y a », « c'est », « ça ».
- **Les mots simples** : « a écrit » (pas « a rédigé/signé »), « a déménagé » (pas « s'est relocalisé »), « utilisé » (pas « mobilisé/exploité »), « a essayé » (pas « s'est attaché à »), « est mort » (pas « s'est éteint », « nous a quittés »).
- **Les superlatifs assumés et affirmations tranchées** : « l'un des meilleurs », « le seul », « le premier », « franchement mauvais ».
- **Les modalisateurs parlés** : « très », « peut-être », « a tendance à », « je crois ».
- **Les détails spécifiques infabricables** : dates précises, montants, chemins de fichiers, « 900 ms → 40 ms », le café « tiède et trop sucré ».
- **Les sentiments mitigés et irrésolus** : « c'est pratique mais laid », « je ne sais pas trop quoi en penser ».
- **Les incises authentiques** : « enfin, je crois », « bon, bref », « on verra bien ».
- **L'oralité de registre** : « du coup », « bref », « perso », « c'est pas » en contexte informel.
- **Les imperfections délibérées** : répétition stylistique voulue, digression assumée, phrase qui claque, fin abrupte.
- **La voix d'époque ou de communauté** : argot de métier, références datées, tics générationnels.

**Si un passage a déjà un pouls, la bonne édition est souvent : aucune.**

## 4. Patterns FAIBLES — ne déclenchent jamais seuls

Un ou deux de ces marqueurs isolés = texte humain, ne rien faire :
- guillemets anglais ou droits isolés (habitude clavier, macOS, Word) ;
- UN tiret cadratin d'incise (typographie française correcte) ;
- UNE triade (rhétorique classique française) ;
- la variation de synonymes (tradition scolaire française — LE faux positif nᵒ 1 du FR) ;
- UN connecteur en tête de phrase ;
- une casse de titre douteuse isolée ;
- un « Excellente question » en vraie conversation ;
- un mot Tier 2 ou Tier 3 du lexique (lexique.md).

## 5. Seuil de déclenchement global

- **0 pattern, ou 1-2 patterns faibles** → « Texte déjà humain — rien à corriger. » STOP. Proposer un diagnostic --dry-run si l'utilisateur insiste, mais rappeler que réécrire du texte humain le dégrade.
- **Signaux moyens sans aucun signal fort** : 1-2 → rien (texte humain) ; 3+ moyens en cluster → traiter comme un fort isolé (retouche ciblée au plus).
- **1 pattern fort isolé** (hors famille A) → suspicion : retouche ciblée de CE passage uniquement, rien d'autre.
- **2+ patterns forts, ou 1 fort + 2 moyens, en cluster** → traitement complet.
- **Famille A (artefacts)** → intervention immédiate quel que soit le reste (seule exception à la règle du faisceau).
- **< 40 mots** → refuser de statuer (« pas assez de signal ») ; corriger seulement ce qui est explicitement demandé.

## 6. Style hétérogène : ne réécrire que les segments suspects

L'alternance passages-parfaits / passages-fautifs signale un texte HYBRIDE (l'humain qui raccorde des blocs générés). Doctrine Wikipédia FR : le contraste EST le marqueur — et le traitement est LOCAL. Ne réécrire que les segments qui cochent le faisceau, préserver intégralement les segments humains (y compris leurs fautes : elles appartiennent à l'auteur ; les signaler séparément si demandé).

## 7. L'anti-contamination : les « faux traits humains »

En dé-IA-isant, on peut INJECTER d'autres tics : fausse candeur (« je ne vais pas vous mentir »), punchlines artificielles, drame fabriqué, oralité plaquée (« ça pique »), anecdotes inventées, chiffres « plausibles ». C'est le piège de l'auto-contamination : le texte troque un slop contre un autre. Garde-fous :
- ne rien ajouter qui ne soit dans le texte source ou fourni par l'auteur (règle anti-fabrication, SKILL.md) ;
- après réécriture, re-scanner sa PROPRE sortie avec ce même catalogue (gate final) ;
- les résidus détectés à l'auto-audit se SUPPRIMENT, ne se justifient pas (« ce registre en a besoin », « ça ferait vide sans » = rationalisations types) ;
- jamais plus de 2 passes : au-delà, on sur-édite vers de la prose hachée et morte.

## 8. Les détecteurs automatiques ne font pas foi

Variance documentée entre relances d'un même prompt : 99 % → 23 %. Même texte scoré 0 % en anglais et 100 % en français par le même outil. Sorties de modèles récents régulièrement classées « humaines ». malherbe n'utilise JAMAIS un score de détecteur comme critère, ne promet jamais l'indétectabilité, et rappelle que le seul test décisif d'un texte suspect est la vérification des faits et des sources.
