#!/usr/bin/env python3
"""audit.py — compteurs déterministes de malherbe (stdlib uniquement, aucun réseau).

Réplique les compteurs du gate final de SKILL.md pour vérification externe et CI.
Ne rend PAS de verdict « IA ou humain » : il chiffre des familles de marqueurs
pour comparer deux versions d'un texte ou vérifier l'invariant typographique.
Un marqueur isolé ne prouve rien — raisonner en grappes (voir SKILL.md).

Usage :
    python3 audit.py texte.md               # compteurs d'un fichier
    python3 audit.py avant.md apres.md      # comparaison + invariant typographique

Sortie : rapport texte sur stdout. Code retour 1 si l'invariant typographique
est violé en mode comparaison (conversion « » / ’ / insécables / majuscules
accentuées vers leurs formes dégradées), 0 sinon.
"""

import re
import statistics
import sys

APOSTROPHE_TYPO = "’"

# --- Marqueurs (lecture littérale ; sous-ensemble stable du catalogue) -------
# Les marqueurs sont écrits avec l'apostrophe droite ; le texte analysé est
# normalisé (’ → ') AVANT le matching, mais compte_typo() et l'invariant
# travaillent sur le texte BRUT (ils doivent voir les ’).

CHEVILLES = [  # R1-R2
    r"il est (?:important|essentiel|crucial|intéressant) de (?:noter|souligner|rappeler|remarquer)",
    r"il convient de (?:noter|souligner|rappeler|mentionner|préciser)",
    r"il est à noter",
    r"force est de constater",
    r"notons que",
    r"précisons que",
    r"il faut savoir que",
    r"dans cette optique",
    r"dans ce cadre",
    r"afin de pouvoir",
    r"dans le cadre de la mise en (?:place|œuvre)",
    r"à l'heure actuelle",
    r"a la capacité de",
]

CONTRASTES = [  # S2
    r"ce n'est pas (?:seulement |simplement |qu'un |qu'une )?[^.!?]{3,60}, (?:c'est|mais)",
    r"non seulement [^.!?]{3,80}mais (?:aussi|également|encore)",
    r"il ne s'agit pas (?:seulement |uniquement )?de [^.!?]{3,60}, mais",
    r"la (?:vraie )?question n'est pas",
    r"le vrai sujet n'est pas",
    r"loin d'être",
    r"n'est pas une fatalité",
]

TIER1 = [  # L1 — suspects dès la première occurrence (portée limitée au catalogue)
    r"dans un monde en (?:constante|perpétuelle) (?:évolution|mutation)",
    r"à l'ère (?:du numérique|du digital|de l'IA|de l'intelligence artificielle)",
    r"dans le paysage \w+ en constante évolution",
    r"plongeons dans",
    r"plongez dans",
    r"exploration approfondie",
    r"joue un rôle crucial",
    r"marque un tournant (?:majeur|décisif)",
    r"témoigne de l'engagement",
    r"empreinte indélébile",
    r"véritable levier de croissance",
    r"libérer (?:tout )?(?:le|votre) potentiel",
    r"débloquer (?:tout )?(?:le|votre) potentiel",
]

TIER2 = [  # L1b — lemmes à suffixes optionnels, densité rapportée /1000 mots
    r"crucia(?:l|le|les|ux)",
    r"essentiel(?:le)?s?",
    r"fondamenta(?:l|le|les|ux)",
    r"incontournables?",
    r"primordia(?:l|le|les|ux)",
    r"pivota(?:l|le|les|ux)",
    r"captivant(?:e)?s?",
    r"fascinant(?:e)?s?",
    r"révolutionnaires?",
    r"disrupti(?:f|ve)s?",
    r"robustes?",
    r"innovant(?:e)?s?",
    r"vibrant(?:e)?s?",
    r"pérennes?",
    r"transformateurs?",
    r"transformatrices?",
]

PARTICIPES = (  # S5 — participes analytiques plaqués après virgule
    r",\s+(?:soulignant|témoignant|illustrant|reflétant|garantissant|offrant|"
    r"permettant|favorisant|contribuant|renforçant|incarnant|symbolisant|"
    r"assurant|facilitant|ouvrant|s'inscrivant|alliant)\b"
)

CONNECTEURS_TETE = (  # S4 — en tête de phrase ou de ligne
    r"(?m)(?:^|[.!?]\s+)(?:Par ailleurs|De plus|En outre|En effet|Ainsi|"
    r"Par conséquent|De ce fait|En somme|En définitive|Dès lors|Qui plus est)\b"
)

CALQUES = [  # C1
    r"adresser (?:un|le|ce|cette) (?:problème|problématique|sujet|question)",
    r"faire du sens",
    r"fait du sens",
    r"délivrer de la valeur",
    r"basé[e]?s? sur",
    r"en termes de",
    r"être en charge de",
]

ARTEFACTS = [  # A1-A3 — preuves quasi certaines
    r"oaicite",
    r"contentReference",
    r"citeturn\d",
    r"utm_source=chatgpt\.com",
    r"utm_source=openai",
    r"referrer=grok\.com",
    r"\[cite:\s*\d",
    r"grok-card",
    r"【\d+†L",
    r"\[attached_file:",
    r":::(?:writing|écriture)\{",
    r"\[(?:Votre nom|Insert Name|à compléter|Nom de l'entreprise)\]",
]

# Virgule d'Oxford : au moins deux items d'énumération avant « , et »
OXFORD = r",\s+[^,;.!?\n]{1,40},\s+et\s+"

MAJUSCULES_ACCENTUEES = "ÀÂÄÉÈÊËÎÏÔÖÙÛÜÇŒÆ"

# --- Typographie -------------------------------------------------------------


def compte_typo(texte):
    """Caractères typographiques français à ne jamais dégrader (texte BRUT)."""
    return {
        "guillemets « »": texte.count("«") + texte.count("»"),
        "apostrophes typographiques": texte.count(APOSTROPHE_TYPO),
        "espaces insécables (U+00A0/U+202F)": texte.count(" ") + texte.count(" "),
        "majuscules accentuées": sum(1 for c in texte if c in MAJUSCULES_ACCENTUEES),
    }


def formes_degradees(texte):
    """Formes DÉGRADÉES correspondant à chaque compteur français.

    Une baisse d'un compteur français peut venir d'une suppression légitime de
    passage. La dégradation n'est avérée que si la forme anglicisée/dactylo
    correspondante AUGMENTE en face (conversion « » → ", ’ → ', É → E…).
    """
    return {
        "guillemets « »": len(re.findall(r"[\"“”](?=[^\n]*[a-zà-ü])", texte)),
        "apostrophes typographiques": len(
            re.findall(r"[a-zà-üA-ZÀ-Ü]'[a-zà-ü]", texte)
        ),
        "espaces insécables (U+00A0/U+202F)": len(re.findall(r" [;:!?»]", texte)),
        "majuscules accentuées": len(
            re.findall(
                r"\b(?:Etat|Eglise|Ecole|Evolution|Etude|Etape|Ere|Age|A(?=\s[a-zà-ü]))\b",
                texte,
            )
        ),
    }


def erreurs_typo(texte):
    """Erreurs typiques d'anglicisation (voir typographie.md)."""
    n = 0
    n += len(re.findall(r"\d+%", texte))  # 50% collé
    n += len(
        re.findall(r"(?<![\w.])\d+\.\d+(?![\d.])", texte)
    )  # 3.14 décimal (pas 1.0.0 ni python3.11)
    n += len(re.findall(r"[€$]\s?\d[\d,]*", texte))  # €1,500
    n += len(re.findall(r"\b(?:Etat|Eglise|Ecole|Evolution|Etude|Etape)\b", texte))
    n += len(
        re.findall(
            r"\b(?:[A-ZÀ-Ü][a-zà-ü]+\s+){2,}(?:De|Du|La|Le|Les|Et|Pour|Dans)\s+[A-ZÀ-Ü]",
            texte,
        )
    )  # Title Case
    n += len(re.findall(OXFORD, texte))  # virgule d'Oxford
    return n


# --- Analyse -----------------------------------------------------------------


def prose_seule(texte):
    """Retire les lignes structurelles (titres, puces, tableaux, citations MD)
    pour que les statistiques de phrases portent sur la prose."""
    return "\n".join(
        l
        for l in texte.splitlines()
        if not re.match(r"\s*(#{1,6} |[-*+] |\||```|---)", l)
    )


def phrases(texte):
    brut = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", prose_seule(texte)))
    return [p for p in brut if len(p.split()) >= 2]


def compte(patterns, texte, flags=re.IGNORECASE):
    return sum(len(re.findall(p, texte, flags)) for p in patterns)


def analyse(texte_brut, nom):
    # Normalisation pour le matching des marqueurs UNIQUEMENT :
    # un texte typographiquement correct (’) doit compter autant qu'un texte en '.
    texte = texte_brut.replace(APOSTROPHE_TYPO, "'")
    mots = len(texte.split())
    ph = phrases(texte)
    longueurs = [len(p.split()) for p in ph]
    tier2 = sum(len(re.findall(rf"\b{m}\b", texte, re.IGNORECASE)) for m in TIER2)

    r = {
        "mots": mots,
        "phrases (prose)": len(ph),
        "artefacts (A — quasi certains)": compte(ARTEFACTS, texte, 0),
        "chevilles R1-R2": compte(CHEVILLES, texte),
        "contrastes S2": compte(CONTRASTES, texte),
        "lexique Tier 1": compte(TIER1, texte),
        "lexique Tier 2 / L1b (brut)": tier2,
        "lexique Tier 2 /1000 mots": round(tier2 * 1000 / mots, 1)
        if mots >= 200
        else "n. s. (texte court)",
        "participes plaqués S5": len(re.findall(PARTICIPES, texte, re.IGNORECASE)),
        "connecteurs en tête S4": len(re.findall(CONNECTEURS_TETE, texte)),
        "calques C1": compte(CALQUES, texte),
        "erreurs typo anglicisées": erreurs_typo(texte),
    }
    if longueurs:
        r["longueurs de phrases"] = longueurs
        r["étalement (max−min)"] = max(longueurs) - min(longueurs)
        r["écart-type des longueurs"] = round(statistics.pstdev(longueurs), 1)
        bande = sum(1 for n in longueurs if 10 <= n <= 20)
        r["part 10-20 mots"] = f"{round(100 * bande / len(longueurs))} %"
    print(f"\n=== {nom} ===")
    for k, v in r.items():
        print(f"  {k:<38} {v}")
    return r


def invariant(avant, apres):
    """VIOLATION = le compteur français baisse ET la forme dégradée correspondante
    augmente (conversion). Une baisse seule = AVERTISSEMENT (passage supprimé ?)."""
    a, b = compte_typo(avant), compte_typo(apres)
    da, db = formes_degradees(avant), formes_degradees(apres)
    print("\n=== Invariant typographique (jamais de dégradation) ===")
    ok = True
    for k in a:
        baisse = b[k] < a[k]
        conversion = db[k] > da[k]
        if baisse and conversion:
            statut, ok = "VIOLATION (conversion détectée)", False
        elif baisse:
            statut = "avertissement (baisse sans conversion — passage supprimé ?)"
        else:
            statut = "OK"
        print(f"  {k:<38} {a[k]} → {b[k]}   {statut}")
    return ok


def main():
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    textes = []
    for chemin in sys.argv[1:]:
        with open(chemin, encoding="utf-8") as f:
            textes.append(f.read())
    analyse(textes[0], sys.argv[1])
    if len(textes) == 2:
        analyse(textes[1], sys.argv[2])
        if not invariant(textes[0], textes[1]):
            print("\nÉCHEC : dégradation typographique détectée.")
            sys.exit(1)
        print("\nInvariant respecté.")
    sys.exit(0)


if __name__ == "__main__":
    main()
