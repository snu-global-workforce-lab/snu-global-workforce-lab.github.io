# News update workflow

There are two supported ways to add news.

## Option 1: GitHub web form

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Select **Create news post**.
4. Click **Run workflow**.
5. Fill in:
   - `title`: News title.
   - `date`: Publication date, such as `2026-06-15`.
   - `excerpt`: Short text shown on the News page.
   - `categories`: Optional comma-separated tags. `news` is added automatically.
   - `image_urls`: Optional comma-separated image URLs. The first image becomes the card thumbnail.
   - `body`: Main post body in Markdown or HTML.

The workflow creates the Markdown post, downloads the linked images into `images/news`, commits the files, and pushes them to the website.

## Option 2: Local folder import

Create one folder for one news item. Put these files in the folder:

- `title.txt` required.
- `date.txt` optional. If omitted, today's date is used.
- `excerpt.txt` optional.
- `categories.txt` optional, comma-separated.
- `body.md` optional.
- Image files optional: `.jpg`, `.jpeg`, `.png`, `.gif`, or `.webp`.

Then run this from the repository root:

```bash
python3 tools/import_news_folder.py "/path/to/news-folder"
```

The script copies images into `images/news`, creates the `_posts/YYYY-MM-DD-title.md` file, and uses the first image as the News card thumbnail.

After checking the generated post, commit and push the changes:

```bash
git add _posts images/news
git commit -m "Add news post"
git push
```

When working through Codex, you can also put the folder on your Desktop and say: "Add this folder as a news update." Codex can run the import, review the generated files, commit, and push.
