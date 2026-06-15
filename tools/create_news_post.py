import json
import os
import re
import shutil
import unicodedata
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen


def env(name, default=""):
    return os.environ.get(name, default).strip()


def yaml_string(value):
    return json.dumps(value or "", ensure_ascii=False)


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug[:70].strip("-") or "news"


def split_list(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_date(date):
    if not date:
        return datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError as exc:
        raise SystemExit("NEWS_DATE must use YYYY-MM-DD format.") from exc

    return date


def image_extension(path_or_url):
    suffix = Path(urlparse(path_or_url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        return suffix
    return ".jpeg"


def destination_path(date, slug, index, source):
    suffix = image_extension(source)
    return Path("images/news") / f"{date}-{slug}-{index}{suffix}"


def copy_image_files(image_paths, date, slug):
    copied = []
    Path("images/news").mkdir(parents=True, exist_ok=True)

    for index, image_path in enumerate(image_paths, start=1):
        source = Path(image_path).expanduser()
        if not source.exists():
            raise SystemExit(f"Image file does not exist: {source}")

        target = destination_path(date, slug, index, str(source))
        if target.exists():
            raise SystemExit(f"{target} already exists. Rename the image or change the title/date.")
        shutil.copy2(source, target)
        copied.append(f"/{target.as_posix()}")

    return copied


def download_image_urls(image_urls, date, slug):
    downloaded = []
    Path("images/news").mkdir(parents=True, exist_ok=True)

    for index, image_url in enumerate(image_urls, start=1):
        target = destination_path(date, slug, index, image_url)
        if target.exists():
            raise SystemExit(f"{target} already exists. Rename the image or change the title/date.")

        with urlopen(image_url, timeout=30) as response:
            target.write_bytes(response.read())
        downloaded.append(f"/{target.as_posix()}")

    return downloaded


def image_tag(image_url, title, top_margin="10px"):
    return (
        f'<img src="{{{{ {yaml_string(image_url)} | relative_url }}}}" '
        f'alt="{title}" '
        f'style="width:100%; height:auto; border-radius:10px; margin: {top_margin} 0 22px 0;">'
    )


def create_post(title, date="", excerpt="", categories=None, teaser="", body="", image_paths=None, image_urls=None):
    if not title:
        raise SystemExit("NEWS_TITLE is required.")

    date = validate_date(date)
    slug = slugify(title)
    categories = categories or ["news"]
    if "news" not in categories:
        categories.insert(0, "news")

    copied_images = copy_image_files(image_paths or [], date, slug)
    downloaded_images = download_image_urls(image_urls or [], date, slug)
    post_images = copied_images + downloaded_images
    teaser = teaser or (post_images[0] if post_images else "")

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

    for index, image_url in enumerate(post_images):
        content_parts.append(image_tag(image_url, title, "10px" if index == 0 else "24px"))
        content_parts.append("")

    content_parts.append(body or excerpt or "")
    content_parts.append("")

    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text("\n".join(content_parts), encoding="utf-8")
    print(f"Created {post_path}")
    for image_url in post_images:
        print(f"Added {image_url}")


def main():
    create_post(
        title=env("NEWS_TITLE"),
        date=env("NEWS_DATE"),
        excerpt=env("NEWS_EXCERPT"),
        categories=split_list(env("NEWS_CATEGORIES", "news")),
        teaser=env("NEWS_TEASER_IMAGE"),
        body=env("NEWS_BODY"),
        image_paths=split_list(env("NEWS_IMAGE_PATHS")),
        image_urls=split_list(env("NEWS_IMAGE_URLS")),
    )


if __name__ == "__main__":
    main()
