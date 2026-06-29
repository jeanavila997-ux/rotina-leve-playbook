import os
import shutil
import markdown
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = os.path.join(BASE_DIR, "content", "playbook.md")
OUTPUT = os.path.join(BASE_DIR, "content", "rotina-leve-playbook.pdf")
OUTPUT_WEB = os.path.join(BASE_DIR, "landing", "assets", "rotina-leve-playbook.pdf")

CSS = """
@page {
    size: A4;
    margin: 24mm 18mm 28mm 18mm;
    @bottom-center {
        content: counter(page);
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 10px;
        color: #64748B;
    }
}

* { box-sizing: border-box; }

body {
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 11pt;
    line-height: 1.65;
    color: #1e293b;
    background: #fff;
}

h1 {
    font-family: 'Sora', 'Inter', sans-serif;
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-top: 0;
    margin-bottom: 12pt;
    page-break-after: avoid;
}

h2 {
    font-family: 'Sora', 'Inter', sans-serif;
    font-size: 16pt;
    font-weight: 700;
    color: #4f46e5;
    margin-top: 22pt;
    margin-bottom: 10pt;
    page-break-after: avoid;
}

h3 {
    font-size: 13pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 16pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
}

p {
    margin: 0 0 10pt 0;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

ul, ol {
    margin: 8pt 0 12pt 0;
    padding-left: 20pt;
}

li {
    margin-bottom: 4pt;
}

blockquote {
    margin: 14pt 0;
    padding: 12pt 16pt;
    border-left: 4px solid #6366f1;
    background: #f5f7fb;
    color: #334155;
    font-style: italic;
    page-break-inside: avoid;
}

hr {
    border: 0;
    border-top: 1px solid #cbd5e1;
    margin: 24pt 0;
    page-break-after: always;
}

strong {
    font-weight: 700;
    color: #0f172a;
}

.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    text-align: center;
    background: linear-gradient(160deg, #312E81 0%, #4F46E5 45%, #0E7490 100%);
    color: white;
    padding: 60px 40px;
    margin: -24mm -18mm 0 -18mm;
}

.cover h1 {
    font-family: 'Sora', 'Inter', sans-serif;
    font-size: 42pt;
    font-weight: 800;
    color: white;
    margin-bottom: 10pt;
    line-height: 1;
}

.cover .subtitle {
    font-size: 15pt;
    color: rgba(255,255,255,0.9);
    font-weight: 500;
}

.cover .tag {
    margin-top: 28pt;
    display: inline-block;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
    padding: 6pt 12pt;
    border-radius: 6pt;
    font-size: 10pt;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.cover .author {
    margin-top: 60pt;
    font-size: 11pt;
    color: rgba(255,255,255,0.7);
}
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Rotina Leve — Playbook Anti-Procrastinação</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  <div class="cover">
    <h1>Rotina Leve</h1>
    <p class="subtitle">Playbook Anti-Procrastinação para Mentes Aceleradas</p>
    <span class="tag">Método Prático de 7 Dias</span>
    <p class="author">Edição Premium</p>
  </div>
  {content}
</body>
</html>
"""


def export_pdf():
    if not os.path.exists(INPUT):
        print(f"Arquivo não encontrado: {INPUT}")
        return

    with open(INPUT, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=["extra", "toc"])
    html = HTML_TEMPLATE.format(css=CSS, content=html_body)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.pdf(
            path=OUTPUT,
            format="A4",
            print_background=True,
            margin={"top": "24mm", "right": "18mm", "bottom": "28mm", "left": "18mm"},
        )
        browser.close()

    # Copia o PDF gerado para a raiz web (landing/assets)
    os.makedirs(os.path.dirname(OUTPUT_WEB), exist_ok=True)
    shutil.copyfile(OUTPUT, OUTPUT_WEB)
    print(f"PDF copiado para a pasta da landing page: {OUTPUT_WEB}")

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"PDF gerado com sucesso: {OUTPUT}")
    print(f"Tamanho: {size_kb:.1f} KB")


if __name__ == "__main__":
    export_pdf()
