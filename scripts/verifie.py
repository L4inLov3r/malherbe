#!/usr/bin/env python3
"""verifie.py — contrôles d'intégrité déterministes du dépôt malherbe (CI).

Vérifie ce qui est vérifiable sans LLM :
  1. Intégrité référentielle : tout ID de pattern référencé (SKILL.md, fixtures,
     références croisées) est défini quelque part dans references/.
  2. Le décompte de patterns annoncé dans SKILL.md correspond au décompte réel.
  3. Invariants à l'octet : les caractères typographiques réels (U+00A0, U+202F,
     U+2019) sont présents là où le dépôt affirme qu'ils le sont.
  4. Frontmatter : allowed-tools au format scalaire attendu.
  5. Chaînes interdites (régressions connues).
  6. scripts/audit.py s'exécute sans erreur sur les fixtures.

Usage : python3 scripts/verifie.py   (depuis la racine du dépôt)
Code retour : 0 si tout passe, 1 sinon.
"""

import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
ECHECS = []


def echec(msg):
    ECHECS.append(msg)
    print(f"  ÉCHEC  {msg}")


def ok(msg):
    print(f"  ok     {msg}")


def lire(chemin):
    return (RACINE / chemin).read_text(encoding="utf-8")


# --- 1. Intégrité référentielle ---------------------------------------------

print("\n[1] Intégrité référentielle des IDs de patterns")

definis = {"L1b"}  # alias documenté dans lexique.md
for f in sorted((RACINE / "references").glob("*.md")):
    t = f.read_text(encoding="utf-8")
    definis |= set(re.findall(r"^#{2,3}\s+([ALCSRFMT]\d{1,2})\b", t, re.M))
    if f.name == "typographie.md":
        definis |= set(re.findall(r"^\|\s*(T\d{1,2})\s*\|", t, re.M))

references = set()
for chemin in ["SKILL.md", "tests/fixtures.md"] + [
    f"references/{f.name}" for f in sorted((RACINE / "references").glob("*.md"))
]:
    t = lire(chemin)
    for m in re.findall(r"\b([ALCSRFMT]\d{1,2}b?)\b", t):
        references.add(m)

inconnus = sorted(r for r in references if r not in definis)
if inconnus:
    echec(f"IDs référencés mais définis nulle part : {inconnus}")
else:
    ok(f"{len(references)} IDs référencés, tous définis ({len(definis)} définitions)")

# --- 2. Décompte annoncé vs réel --------------------------------------------

print("\n[2] Décompte des patterns")
reels = len(definis - {"L1b"})
skill = lire("SKILL.md")
m = re.search(r"\((\d+) patterns\)", skill)
if not m:
    echec("Décompte annoncé introuvable dans SKILL.md")
elif int(m.group(1)) != reels:
    echec(f"SKILL.md annonce {m.group(1)} patterns, le dépôt en définit {reels}")
else:
    ok(f"{reels} patterns définis = décompte annoncé")

# --- 3. Invariants à l'octet -------------------------------------------------

print("\n[3] Invariants typographiques à l'octet")
typo = lire("references/typographie.md")
fixtures = lire("tests/fixtures.md")

for nom, texte, char, minimum in [
    ("typographie.md U+00A0", typo, " ", 1),
    ("typographie.md U+202F", typo, " ", 1),
    ("typographie.md U+2019", typo, "’", 8),
    ("fixtures.md U+00A0 (SNF soignées)", fixtures, " ", 7),
    ("fixtures.md U+202F (SNF soignées)", fixtures, " ", 3),
]:
    n = texte.count(char)
    if n < minimum:
        echec(f"{nom} : {n} occurrence(s), minimum {minimum}")
    else:
        ok(f"{nom} : {n} ≥ {minimum}")

for tag in ("SNF-7", "SNF-9", "SNF-12", "SNF-13"):
    bloc = fixtures.split(f"### {tag}")[1].split("###")[0]
    lignes = [l for l in bloc.splitlines() if l.startswith(">")]
    droites = sum(l.count("'") for l in lignes)
    if droites:
        echec(
            f"{tag} : {droites} apostrophe(s) droite(s) dans un texte annoncé « au caractère près »"
        )
    else:
        ok(f"{tag} : apostrophes typographiques uniquement")

# --- 4. Frontmatter -----------------------------------------------------------

print("\n[4] Frontmatter SKILL.md")
if re.search(r"^allowed-tools: Read, Write, Edit, Grep, Glob$", skill, re.M):
    ok("allowed-tools au format scalaire attendu")
else:
    echec(
        "allowed-tools absent ou pas au format scalaire « Read, Write, Edit, Grep, Glob »"
    )

# --- 5. Chaînes interdites ----------------------------------------------------

print("\n[5] Chaînes interdites (régressions connues)")
INTERDITES = ["suppprim", "Directité", "Voice Read", "~70 patterns"]
cibles = ["SKILL.md", "README.md", "CHANGELOG.md", "tests/fixtures.md"] + [
    f"references/{f.name}" for f in sorted((RACINE / "references").glob("*.md"))
]
trouvees = []
for chemin in cibles:
    t = lire(chemin)
    for s in INTERDITES:
        if s in t:
            trouvees.append(f"{chemin} : « {s} »")
if trouvees:
    for t in trouvees:
        echec(t)
else:
    ok("aucune chaîne interdite")

# --- 6. Cohérence des versions -------------------------------------------------

print("\n[6] Cohérence des versions")
v_skill = re.search(r"^version: ([\d.]+)$", skill, re.M)
v_chlog = re.search(r"^## ([\d.]+) ", lire("CHANGELOG.md"), re.M)
v_readme = re.search(r"badge/version-([\d.]+)-", lire("README.md"))
versions = {
    "SKILL.md frontmatter": v_skill and v_skill.group(1),
    "CHANGELOG.md (1re entrée)": v_chlog and v_chlog.group(1),
    "README.md (badge)": v_readme and v_readme.group(1),
}
if None in versions.values() or len(set(versions.values())) != 1:
    echec(f"versions incohérentes : {versions}")
else:
    ok(f"version {v_skill.group(1)} partout")

# --- 7. audit.py --------------------------------------------------------------

print("\n[7] Exécution de scripts/audit.py sur les fixtures")
r = subprocess.run(
    [
        sys.executable,
        str(RACINE / "scripts" / "audit.py"),
        str(RACINE / "tests" / "fixtures.md"),
    ],
    capture_output=True,
)
if r.returncode != 0:
    echec(f"audit.py a échoué (code {r.returncode}) : {r.stderr.decode()[:200]}")
else:
    ok("audit.py tourne sans erreur")

# --- Bilan --------------------------------------------------------------------

print(f"\n{'ÉCHEC' if ECHECS else 'OK'} — {len(ECHECS)} problème(s)")
sys.exit(1 if ECHECS else 0)
