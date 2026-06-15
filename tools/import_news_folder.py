from pathlib import Path

from create_news_post import create_post, split_list


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Create a news post from a local folder.")
    parser.add_argument("source_dir", help="Folder with title.txt, optional metadata files, body.md, and images.")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser()
    if not source_dir.exists():
        raise SystemExit(f"Folder does not exist: {source_dir}")

    title = read_text(source_dir / "title.txt")
    if not title:
        raise SystemExit(f"{source_dir / 'title.txt'} is required.")

    images = sorted(
        str(path)
        for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )

    create_post(
        title=title,
        date=read_text(source_dir / "date.txt"),
        excerpt=read_text(source_dir / "excerpt.txt"),
        categories=split_list(read_text(source_dir / "categories.txt") or "news"),
        body=read_text(source_dir / "body.md"),
        image_paths=images,
    )


if __name__ == "__main__":
    main()
