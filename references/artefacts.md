# Famille A — Artefacts d'assistant (preuves quasi certaines)

La seule famille où un marqueur ISOLÉ suffit à agir : ce sont des résidus techniques ou conversationnels qui ne peuvent pas apparaître dans un texte écrit par un humain. À vérifier EN PREMIER, par recherche de motifs littéraux (Grep quand le texte est dans un fichier).

Sources : Wikipédia EN « Signs of AI writing » (WP:OAICITE, WP:CERTAINLY, WP:AICUTOFF, WP:AIPLACEHOLDER), Wikipédia FR « Aide:Identifier l'usage d'une IA générative » (cas archivés par l'Observatoire des IA), boileau, ultimate-humanizer.

Correction commune : suppression pure (A1-A4) ou suppression + signalement à l'auteur. Sévérité : **C dans les quatre registres**, sauf mention.

## A1 — Artefacts de balisage interne (preuve technique absolue)

Fuites du code de formatage interne des chatbots. Détection par motifs littéraux :

| Outil | Motifs |
|---|---|
| ChatGPT | `:contentReference[oaicite:` · `oai_citation` · `citeturn0search` · `Wikipedia+1`, `Nom+3` (agrégats de sources) · `attributableIndex` |
| Gemini | `[cite: ` · `[span_1](start_span)` / `(end_span)` |
| Grok | `<grok-card` · `grok_render_citation_card_json` |
| DeepSeek | `【` + chiffres + `†L` (crochets lenticulaires : `【85†L261-269】`) |
| Perplexity | `[attached_file:` · `[web:` · URLs `ppl-ai-file-upload` |
| Divers (2026) | `:::writing{` et sa forme localisée `:::écriture{` |

Aussi : caractères Unicode de zone privée (U+E000-F8FF) entourant des références, caractère ↩ collé aux notes de bas de page.

## A2 — Traces d'outil dans les URLs

`utm_source=chatgpt.com` · `utm_source=openai` · `utm_source=copilot.com` · `referrer=grok.com`. → Retirer LE PARAMÈTRE, jamais l'URL (les UTM posés volontairement par l'auteur — utm_source=newsletter — restent). Prouve l'usage de l'outil pour la recherche de sources, pas forcément pour la rédaction : le signaler avec cette nuance.

## A3 — Placeholders non remplis

`[Votre nom]`, `[Insert Name]`, `[Nom de l'entreprise]`, `[à compléter]`, `2025-XX-XX`, `INSERT_SOURCE_URL`, `[Décrivez ici…]`, champs de gabarit vides. → Signaler à l'auteur (le skill ne peut pas les remplir — il ne connaît pas la réponse).

## A4 — Chapeau ou clôture de chat collés

- Ouvertures : « Voici une version complète de… », « Bien sûr ! Voici… », « Certainement ! », « Voici un article respectant les conventions… », séparateur `---` initial hérité du chat.
- Clôtures : « J'espère que cela vous aide », « N'hésitez pas à me demander », « Souhaitez-vous que je… », « Dites-moi si vous voulez que j'approfondisse », « Si vous le souhaitez, je peux… ».
→ Suppression pure. L'information se suffit à elle-même.

## A5 — Refus de prompt et auto-mise en scène

« En tant que modèle de langage… », « En tant qu'IA, je ne peux pas… mais je peux… », « Je suis désolé, mais… » (en tête de texte). → Supprimer la mise en scène, garder le contenu s'il existe.

## A6 — Avis de coupure de connaissance et spéculation sur les lacunes

« À la date de ma dernière mise à jour », « selon les informations disponibles », « d'après les sources consultées », « les détails ne sont pas largement documentés, mais il est probable que… », « il/elle reste discret(ète) sur sa vie privée » (spéculation inventée sur l'absence d'information — y compris l'affirmation que c'est non documenté). → Supprimer ; si l'information est réellement incertaine, le dire factuellement avec une date (« En mai 2025… ») ou poser un placeholder « (à compléter par l'auteur : …) ».

## A7 — Ton flatteur ou servile (registre conversationnel résiduel)

« Excellente question ! », « Vous avez tout à fait raison », « C'est une remarque très pertinente », « Bien vu ! ». → Ton neutre, entrer dans le sujet.
Sévérité : A:C P:C L:C C:**S** (dans une vraie conversation, « bonne question » peut être sincère — corriger seulement si la flatterie est mécanique ou imméritée).

## A8 — Coupure abrupte

Texte qui s'arrête net en milieu de phrase ou de section (limite de génération). Faux positif possible : copier-coller raté. → Signaler, ne pas « compléter » (compléter serait fabriquer).

## A9 — Balisage du mauvais système

`**gras**` Markdown dans un e-mail ou un doc Word, `[texte](url)` hors Markdown, ` ``` ` visibles, `#` de titres dans un texte de prose, séparateurs `---` hors support Markdown. Indicateur FORT en contexte non-Markdown, FAIBLE en contexte technique (les développeurs écrivent du Markdown partout). → Convertir vers le format du support de destination.

## A10 — Gabarit biographique standardisé (cas FR documenté par Wikipédia)

« X Y (né le JJ mois AAAA) est un auteur, formateur et expert français en…, spécialisé dans… Il est connu pour avoir développé… » — empilement de rôles + spécialisation pompeuse + « il est connu pour ». → Réécrire avec les faits vérifiables fournis ; signaler si la notoriété affirmée n'est adossée à rien.

## Règle de la famille

Un seul marqueur A1-A6 = intervention immédiate, quels que soient le registre et le reste du texte. C'est l'exception à la règle du faisceau d'indices : ces motifs n'existent pas en écriture humaine. En revanche, leur présence signifie aussi que LE FOND doit être vérifié (sources, faits) — le signaler systématiquement : « ce texte contient des artefacts d'outil ; vérifie les faits et les sources, pas seulement le style ».
