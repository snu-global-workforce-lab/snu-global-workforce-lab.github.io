import json
import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path


def env(name, default=""):
    return os.environ.get(name, default).strip()


def yaml_string(value):
    return json.dumps(value or "", ensure_ascii=False)


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug[:70].strip("-") or "news"


title = env("NEWS_TITLE")
date = env("NEWS_DATE")
excerpt = env("NEWS_EXCERPT")
categories = [item.strip() for item in env("NEWS_CATEGORIES", "news").split(",") if item.strip()]
teaser = env("NEWS_TEASER_IMAGE")
body = env("NEWS_BODY")

if not title:
    raise SystemExit("NEWS_TITLE is required.")

if not date:
    date = datetime.utcnow().strftime("%Y-%m-%d")

try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError as exc:
    raise SystemExit("NEWS_DATE must use YYYY-MM-DD format.") from exc

if "news" not in categories:
    categories.insert(0, "news")

slug = slugify(title)
post_path = Path("_posts") / f"{date}-{slug}.md"

if post_path.exists():
    raise SystemExit(f"{post_path} already exists. Change the title or date.")

front_matter = [
    "---",
    f"title: {yaml_string(title)}",
    f"date: {date}",
    f"categories: [{', '.join(yaml_string(category) for category in categories)}]",
]

if excerpt:
    front_matter.append(f"excerpt: {yaml_string(excerpt)}")

if teaser:
    front_matter.extend(
        [
            "header:",
            f"  teaser: {teaser}",
            f"teaser: {teaser}",
        ]
    )

front_matter.append("author_profile: false")
front_matter.append("---")

content_parts = ["\n".join(front_matter), ""]

if teaser:
    content_parts.append(
        f'<img src="{{{{ {yaml_string(teaser)} | relative_url }}}}" '
        'style="width:100%; border-radius:10px; margin: 10px 0 22px 0;">'
    )
    content_parts.append("")

content_parts.append(body or excerpt or "")
content_parts.append("")

post_path.write_text("\n".join(content_parts), encoding="utf-8")
print(f"Created {post_path}")
