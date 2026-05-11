import markdown
import weasyprint
import os

# ── CONFIG ──────────────────────────────────────────
MD_FILE = "merged.md"       # your markdown file
CSS_FILE = "style.css"         # your stylesheet
OUT_FILE = "acp.pdf"   # output PDF name
TITLE = "Advanced Computer Programming"
AUTHOR = "Bidur Sapkota"
YEAR = "2026"
# ────────────────────────────────────────────────────

# Read markdown
with open(MD_FILE, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=[
    "extra",        # tables, fenced code, footnotes
    "codehilite",   # syntax highlighting
    "toc",          # table of contents
    "meta",         # metadata
    "nl2br",        # newline to <br>
])
body_html = md.convert(md_text)

# Fix image paths — remove leading slash
body_html = body_html.replace('src="/', 'src="')

# Read CSS
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css_content = f.read()

# Build full HTML document
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{TITLE}</title>
    <style>{css_content}</style>
</head>
<body>
    {body_html}
</body>
</html>"""

# Save intermediate HTML (optional, for debugging)
with open("preview.html", "w", encoding="utf-8") as f:
    f.write(html)

# Generate PDF
print("Generating PDF...")
weasyprint.HTML(string=html, base_url=os.path.abspath(".")).write_pdf(OUT_FILE)
print(f"Done! Saved as: {OUT_FILE}")
