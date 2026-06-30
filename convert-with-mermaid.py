import os
import markdown
import weasyprint
from pygments.formatters import HtmlFormatter

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

import re
import urllib.request
import ssl
import base64

def process_mermaid(text):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    def replacer(match):
        mermaid_code = match.group(1).strip()
        import json
        
        # 1. Fetch SVG from Kroki just to read its logical width/height
        logical_width = None
        try:
            kroki_req = urllib.request.Request("https://kroki.io/mermaid/svg", data=mermaid_code.encode('utf-8'), headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'text/plain'})
            with urllib.request.urlopen(kroki_req, context=ctx) as k_res:
                svg_data = k_res.read().decode('utf-8')
                width_match = re.search(r'<svg[^>]*width="([^"]+)"', svg_data)
                if width_match:
                    logical_width = float(width_match.group(1).replace('px', ''))
        except Exception:
            pass
            
        style = f"max-width: 100%; height: auto; {'width: ' + str(logical_width) + 'px;' if logical_width else ''}"
        
        # 2. Fetch High-Res PNG from mermaid.ink
        state = {
            "code": mermaid_code,
            "mermaid": {"theme": "default"}
        }
        b64 = base64.urlsafe_b64encode(json.dumps(state).encode('utf-8')).decode('utf-8')
        url = f"https://mermaid.ink/img/{b64}?type=png&bgColor=ffffff&width=2000"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx) as response:
                img_data = response.read()
                img_b64 = base64.b64encode(img_data).decode('utf-8')
                return f'<div style="text-align: center; margin: 20px 0;"><img src="data:image/png;base64,{img_b64}" class="mermaid-diagram" style="{style}" /></div>\n'
        except Exception as e:
            print(f"Error fetching mermaid diagram: {e}")
            return match.group(0)

    pattern = re.compile(r'```mermaid\n(.*?)\n```', re.DOTALL)
    return pattern.sub(replacer, text)

print("Processing mermaid diagrams...")
md_text = process_mermaid(md_text)

pygments_css = HtmlFormatter(style='default').get_style_defs('.codehilite')

# Convert markdown to HTML
md = markdown.Markdown(extensions=[
    "extra",        # tables, fenced code, footnotes
    "codehilite",   # syntax highlighting
    "toc",          # table of contents
    "meta",         # metadata
    "nl2br",        # newline to <br>
    "sane_lists",
], tab_length=2)
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
    <style>
    {css_content}
    {pygments_css}
    </style>
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
