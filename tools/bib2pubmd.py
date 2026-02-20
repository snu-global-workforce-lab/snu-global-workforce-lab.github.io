import re, os, hashlib
from pathlib import Path

BIB_PATH = Path("_data/scholar.bib")
OUT_DIR = Path("_publications")
OUT_DIR.mkdir(exist_ok=True)

def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]

def get_field(entry, key):
    m = re.search(rf"{key}\s*=\s*[{{\"](.+?)[}}\"],", entry, re.S | re.I)
    return m.group(1).replace("\n"," ").strip() if m else ""

bib = BIB_PATH.read_text(encoding="utf-8", errors="ignore")
entries = re.findall(r"@.*?\n}\n?", bib, re.S)

for entry in entries:
    entry_type = re.search(r"@(\w+)", entry).group(1)
    title = get_field(entry, "title")
    year = get_field(entry, "year")
    author = get_field(entry, "author")
    journal = get_field(entry, "journal") or get_field(entry, "booktitle")
    doi = get_field(entry, "doi")

    if not title or not year:
        continue

    slug = slugify(title)
    hid = hashlib.md5((title+year).encode()).hexdigest()[:6]
    filename = OUT_DIR / f"{year}-{slug}-{hid}.md"

    if entry_type.lower() == "article":
        ptype = "Journal Article"
    elif entry_type.lower() in ["incollection","inbook"]:
        ptype = "Book Chapter"
    else:
        ptype = "Working Paper"

    paperurl = f"https://doi.org/{doi}" if doi else ""

    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{slug}-{hid}/
date: {year}-01-01
venue: "{journal}"
type: "{ptype}"
citation: "{author} ({year}). {title}. {journal}."
paperurl: "{paperurl}"
---

"""

    filename.write_text(content, encoding="utf-8")

print("Publications generated.")
