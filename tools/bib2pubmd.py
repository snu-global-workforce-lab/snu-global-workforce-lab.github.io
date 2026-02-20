import re, os, hashlib
from pathlib import Path

BIB_PATH = Path("_data/scholar.bib")
OUT_DIR = Path("_publications")
OUT_DIR.mkdir(exist_ok=True)

# --- Minimal LaTeX → Unicode cleanup (covers common BibTeX exports) ---
LATEX_MAP = {
    r"\"a": "ä", r"\"o": "ö", r"\"u": "ü", r"\"A": "Ä", r"\"O": "Ö", r"\"U": "Ü",
    r"\'a": "á", r"\'e": "é", r"\'i": "í", r"\'o": "ó", r"\'u": "ú",
    r"\`a": "à", r"\`e": "è", r"\`i": "ì", r"\`o": "ò", r"\`u": "ù",
    r"\^a": "â", r"\^e": "ê", r"\^i": "î", r"\^o": "ô", r"\^u": "û",
    r"\~n": "ñ", r"\~a": "ã", r"\~o": "õ",
    r"\c{c}": "ç",
    r"\ss": "ß",
    r"\ae": "æ", r"\AE": "Æ",
    r"\oe": "œ", r"\OE": "Œ",
    r"\aa": "å", r"\AA": "Å",
    r"\o": "ø", r"\O": "Ø",
}

def latex_to_unicode(text: str) -> str:
    if not text:
        return ""
    t = text

    # Replace things like {\"u} or \"{u} or \"u
    # First handle braced accent forms
    t = re.sub(r"\{\\([\"\'\^`~])\s*([A-Za-z])\}", lambda m: LATEX_MAP.get(f"\\{m.group(1)}{m.group(2)}", m.group(2)), t)
    t = re.sub(r"\\([\"\'\^`~])\{([A-Za-z])\}", lambda m: LATEX_MAP.get(f"\\{m.group(1)}{m.group(2)}", m.group(2)), t)

    # Then handle simple accent forms like \"u
    for k, v in LATEX_MAP.items():
        t = t.replace(k, v)

    # Remove leftover braces used for capitalization protection
    t = t.replace("{", "").replace("}", "")

    # Normalize whitespace
    t = re.sub(r"\s+", " ", t).strip()
    return t

def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]

def get_field(entry, key):
    # Matches: key = { ... } or key = " ... "
    m = re.search(rf"{key}\s*=\s*(\{{|\")(.+?)(\}}|\"),", entry, re.S | re.I)
    return m.group(2).replace("\n"," ").strip() if m else ""

def pick_type(entry_type: str) -> str:
    et = entry_type.lower()
    if et == "article":
        return "Journal Article"
    if et in ["incollection", "inbook", "bookchapter"]:
        return "Book Chapter"
    if et in ["techreport", "report"]:
        return "Report"
    return "Working Paper"

bib = BIB_PATH.read_text(encoding="utf-8", errors="ignore")
entries = re.findall(r"@.*?\n}\n?", bib, re.S)

for entry in entries:
    mtype = re.search(r"@(\w+)", entry)
    if not mtype:
        continue
    entry_type = mtype.group(1)

    title = latex_to_unicode(get_field(entry, "title"))
    year = latex_to_unicode(get_field(entry, "year"))
    author = latex_to_unicode(get_field(entry, "author"))
    journal = latex_to_unicode(get_field(entry, "journal") or get_field(entry, "booktitle"))
    doi = latex_to_unicode(get_field(entry, "doi"))

    if not title or not year:
        continue

    slug = slugify(title)
    hid = hashlib.md5((title+year).encode()).hexdigest()[:6]
    filename = OUT_DIR / f"{year}-{slug}-{hid}.md"

    ptype = pick_type(entry_type)

    paperurl = f"https://doi.org/{doi}" if doi else ""

    # Simple readable author string for display (optional)
    # Convert BibTeX "Last, First and Last, First" → "First Last; First Last"
    def author_pretty(a: str) -> str:
        if not a:
            return ""
        parts = [p.strip() for p in a.split(" and ") if p.strip()]
        out = []
        for p in parts:
            if "," in p:
                last, first = [x.strip() for x in p.split(",", 1)]
                out.append(f"{first} {last}".strip())
            else:
                out.append(p)
        return "; ".join(out)

    authors_pretty = author_pretty(author)

    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{slug}-{hid}/
date: {year}-01-01
venue: "{journal}"
type: "{ptype}"
authors: "{authors_pretty}"
paperurl: "{paperurl}"
---

"""
    filename.write_text(content, encoding="utf-8")

print("Publications generated.")
