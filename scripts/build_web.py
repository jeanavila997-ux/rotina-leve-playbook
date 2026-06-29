"""
Compila os capítulos em content/playbook/*.md em um playbook animado (HTML autossuficiente).

Pipeline: content/playbook/*.md -> este script -> landing/playbook.html
"""

import os
import re
import html

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(BASE_DIR, "content", "playbook")
OUTPUT = os.path.join(BASE_DIR, "landing", "playbook.html")


# ---------- parsing ----------

KIND_RULES = [
    ("cenario",   re.compile(r"\bcen[á]rio\b", re.I)),
    ("dor",       re.compile(r"\bdor\b", re.I)),
    ("causa",     re.compile(r"\bpor que\b|\bporque\b|\bpor que isso\b", re.I)),
    ("cerebro",   re.compile(r"c[é]rebro|forma simples", re.I)),
    ("solucao",   re.compile(r"\bsolu[çc][ã]o\b", re.I)),
    ("exercicio", re.compile(r"\bexerc[íi]cio\b", re.I)),
    ("resumo",    re.compile(r"\bresumo\b", re.I)),
    ("transicao", re.compile(r"pr[óo]ximo cap[íi]tulo|caminho para o pr[óo]ximo|o que vem a seguir|vem a seguir", re.I)),
    ("pagina",    re.compile(r"\bp[áa]gina\b", re.I)),
]

KIND_LABEL = {
    "cenario":   "O Cenário",
    "dor":       "A Dor",
    "causa":     "A Causa",
    "cerebro":   "O Cérebro",
    "solucao":   "A Solução",
    "exercicio": "O Exercício",
    "resumo":    "O Resumo",
    "transicao": "O Próximo Passo",
    "pagina":    "Página",
}


def classify(title: str) -> str:
    for kind, rx in KIND_RULES:
        if rx.search(title):
            return kind
    return "texto"


def inline(text: str) -> str:
    """Converte ênfase inline simples para HTML."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*(?!\*)", r"<em>\1</em>", text)
    return text


def render_block(lines: list[str]) -> str:
    """Renderiza um bloco (parágrafo, lista, citação) a partir de linhas não-vazias."""
    if not lines:
        return ""
    first = lines[0].strip()
    if first.startswith(">"):
        quote = "\n".join(l.lstrip("> ").strip() for l in lines if l.strip().startswith(">"))
        return f'<blockquote>{inline(quote)}</blockquote>'
    if re.match(r"^\d+\.\s", first):
        items = "".join(f"<li>{inline(re.sub(r'^\d+\.\s+', '', l.strip()))}</li>" for l in lines if l.strip())
        return f"<ol>{items}</ol>"
    if first.startswith("- "):
        items = "".join(f"<li>{inline(l.strip()[2:])}</li>" for l in lines if l.strip().startswith("-"))
        return f"<ul>{items}</ul>"
    para = " ".join(l.strip() for l in lines)
    return f"<p>{inline(para)}</p>"


def render_body(md: str) -> str:
    """Converte o corpo de uma seção (sem o ##) em HTML."""
    blocks = []
    cur: list[str] = []
    for raw in md.splitlines():
        if raw.strip() == "":
            if cur:
                blocks.append(render_block(cur))
                cur = []
        else:
            cur.append(raw)
    if cur:
        blocks.append(render_block(cur))
    return "\n".join(b for b in blocks if b)


def split_sections(md: str) -> list[tuple[str, str]]:
    """Devolve [(titulo, corpo), ...] a partir do markdown de um capítulo."""
    sections = []
    cur_title = None
    cur_body = []
    for line in md.splitlines():
        if line.startswith("## "):
            if cur_title is not None:
                sections.append((cur_title, "\n".join(cur_body).strip()))
            cur_title = line[3:].strip()
            cur_body = []
        else:
            cur_body.append(line)
    if cur_title is not None:
        sections.append((cur_title, "\n".join(cur_body).strip()))
    return sections


def split_title_header(md: str) -> tuple[str, str]:
    """Extrai o título (# ...) e devolve (titulo, resto)."""
    m = re.match(r"^#\s+(.+?)\s*$", md, re.M)
    if not m:
        return ("Capítulo", md)
    title = m.group(1).strip()
    rest = md[m.end():].lstrip()
    return title, rest


# ---------- capítulos ----------

def natural_key(name: str) -> int:
    m = re.match(r"^(\d+)", name)
    return int(m.group(1)) if m else 999


def load_chapters() -> list[dict]:
    files = sorted(
        [f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md")],
        key=natural_key,
    )
    chapters = []
    for fname in files:
        with open(os.path.join(CHAPTERS_DIR, fname), "r", encoding="utf-8") as f:
            md = f.read().strip()
        if not md:
            continue
        title, rest = split_title_header(md)
        # número do capítulo a partir do título
        nm = re.search(r"(\d+)", title)
        num = int(nm.group(1)) if nm else len(chapters) + 1
        is_parte = title.lower().startswith("parte")
        secs = split_sections(rest)
        sections = []
        for st, sb in secs:
            kind = classify(st)
            sections.append({"title": st, "kind": kind, "body": render_body(sb)})
        chapters.append({
            "num": num,
            "title": title,
            "is_parte": is_parte,
            "sections": sections,
        })
    return chapters


# ---------- HTML ----------

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Rotina Leve — Playbook Animado. O método anti-procrastinação para mentes aceleradas, em uma experiência de leitura que drena o atrito conforme você avança.">
<meta name="theme-color" content="#F6F1E7">
<title>Rotina Leve — Playbook Animado</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
:root {{
  --papel: #F6F1E7;
  --papel-2: #EFE8D8;
--tinta: #1B1A17;
  --tinta-soft: #3A372F;
  --neblina: #E6DECC;
  --atrevo: #E15A2B;
  --atrevo-soft: rgba(225, 90, 43, 0.10);
  --leve: #3E7B6B;
  --leve-soft: rgba(62, 123, 107, 0.10);
  --realce: #C9A86A;
  --line: rgba(27, 26, 23, 0.10);
  --line-2: rgba(27, 26, 23, 0.18);
  --shadow: 0 24px 60px -28px rgba(27, 26, 23, 0.28);
}}

* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}

body {{
  margin: 0;
  background: var(--papel);
  color: var(--tinta);
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  /* grão de papel sutil */
  background-image:
    radial-gradient(rgba(27,26,23,0.025) 1px, transparent 1px),
    radial-gradient(rgba(27,26,23,0.018) 1px, transparent 1px);
  background-size: 3px 3px, 7px 7px;
  background-position: 0 0, 1px 2px;
}}

h1, h2, h3 {{
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
  margin: 0;
  color: var(--tinta);
  font-variation-settings: "opsz" 144;
}}
p {{ margin: 0 0 1.1em; }}
strong {{ font-weight: 700; color: var(--tinta); }}
em {{ font-style: italic; }}
a {{ color: var(--atrevo); }}

.mono {{ font-family: 'JetBrains Mono', ui-monospace, monospace; }}

/* ---------- TOPO / CAPA ---------- */
.cover {{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 24px 120px;
  position: relative;
  overflow: hidden;
}}
.cover .seal {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--realce);
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 36px;
  opacity: 0;
  animation: rise 900ms cubic-bezier(.2,.7,.2,1) 100ms forwards;
}}
.cover .seal::before, .cover .seal::after {{
  content: ""; width: 28px; height: 1px; background: var(--realce); opacity: .6;
}}
.cover h1 {{
  font-size: clamp(56px, 12vw, 148px);
  font-weight: 500;
  letter-spacing: -0.04em;
  line-height: 0.92;
  margin: 0;
  font-variation-settings: "opsz" 144;
  opacity: 0;
  animation: rise 1100ms cubic-bezier(.2,.7,.2,1) 250ms forwards;
}}
.cover h1 .light {{
  font-style: italic;
  font-weight: 400;
  color: var(--leve);
}}
.cover .sub {{
  font-family: 'Fraunces', serif;
  font-size: clamp(18px, 2.4vw, 24px);
  color: var(--tinta-soft);
  max-width: 560px;
  margin: 28px auto 0;
  font-weight: 400;
  opacity: 0;
  animation: rise 1100ms cubic-bezier(.2,.7,.2,1) 450ms forwards;
}}
.cover .meta {{
  margin-top: 56px;
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
  justify-content: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.08em;
  color: var(--tinta-soft);
  text-transform: uppercase;
  opacity: 0;
  animation: rise 1100ms cubic-bezier(.2,.7,.2,1) 650ms forwards;
}}
.cover .meta span {{ display: inline-flex; align-items: center; gap: 8px; }}
.cover .meta .dot {{ width: 6px; height: 6px; border-radius: 50%; background: var(--atrevo); }}
.cover .meta .dot.leve {{ background: var(--leve); }}

.scroll-cue {{
  position: absolute;
  bottom: 34px;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.2em;
  color: var(--tinta-soft);
  text-transform: uppercase;
  opacity: 0;
  animation: rise 900ms ease 900ms forwards, bob 2.4s ease-in-out 1.8s infinite;
}}
.scroll-cue::after {{
  content: ""; display: block; width: 1px; height: 26px; margin: 10px auto 0;
  background: linear-gradient(var(--tinta-soft), transparent);
}}

@keyframes rise {{
  from {{ opacity: 0; transform: translateY(18px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes bob {{
  0%,100% {{ transform: translate(-50%, 0); }}
  50%     {{ transform: translate(-50%, 7px); }}
}}

/* ---------- TRILHO ---------- */
.rail {{
  position: fixed;
  top: 0; left: 0; bottom: 0;
  width: 280px;
  background: var(--papel-2);
  border-right: 1px solid var(--line);
  overflow-y: auto;
  padding: 34px 26px 60px;
  z-index: 30;
}}
.rail .brand {{
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin-bottom: 4px;
}}
.rail .brand .light {{ font-style: italic; color: var(--leve); font-weight: 500; }}
.rail .brand-sub {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--tinta-soft);
  margin-bottom: 30px;
}}
.rail .progress-label {{
  display: flex; justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--tinta-soft);
  margin-bottom: 8px;
}}
.rail .progress-track {{
  height: 3px; background: var(--neblina); border-radius: 999px; overflow: hidden;
}}
.rail .progress-fill {{
  height: 100%; width: 0%;
  background: linear-gradient(90deg, var(--atrevo), var(--leve));
  transition: width .15s linear;
}}
.rail .toc-title {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--tinta-soft);
  margin: 28px 0 12px;
}}
.rail ol {{
  list-style: none; margin: 0; padding: 0;
}}
.rail li {{
  margin: 0;
}}
.rail a {{
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 7px 10px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--tinta-soft);
  font-size: 13.5px;
  line-height: 1.35;
  transition: background .18s, color .18s, transform .18s;
  border-left: 2px solid transparent;
}}
.rail a:hover {{
  background: var(--papel);
  color: var(--tinta);
  transform: translateX(2px);
}}
.rail a .n {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--realce);
  flex: 0 0 22px;
}}
.rail a.active {{
  background: var(--papel);
  color: var(--tinta);
  border-left-color: var(--atrevo);
  font-weight: 600;
}}
.rail a.active .n {{ color: var(--atrevo); }}

/* ---------- LEITURA ---------- */
.reader {{
  margin-left: 280px;
  padding: 0 0 120px;
}}
.reader > * {{ max-width: 720px; margin-left: auto; margin-right: auto; padding-left: 56px; padding-right: 56px; }}

.chapter {{
  position: relative;
  padding-top: 110px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--line);
}}
.chapter:last-of-type {{ border-bottom: 0; }}

.chapter-head {{
  position: relative;
  margin-bottom: 56px;
}}
.chapter-head .num {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.24em;
  color: var(--realce);
  text-transform: uppercase;
  display: block;
  margin-bottom: 18px;
}}
.chapter-head .num .of {{ color: var(--tinta-soft); opacity: .6; }}
.chapter-head h2 {{
  font-size: clamp(30px, 4.4vw, 44px);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.08;
  max-width: 640px;
}}
.chapter-head .num-line {{
  width: 56px; height: 2px; background: var(--atrevo); margin-top: 26px; opacity: .85;
}}

/* assinatura: medidor de atrito */
.atrito {{
  position: absolute;
  top: 150px;
  right: -28px;
  width: 4px;
  height: calc(100% - 200px);
  background: var(--neblina);
  border-radius: 999px;
  overflow: hidden;
}}
.atrito-fill {{
  position: absolute;
  inset: 0 0 0 0;
  background: linear-gradient(180deg, var(--atrevo) 0%, var(--atrevo) 40%, var(--leve) 100%);
  transform: translateY(100%);
  transition: transform .12s linear;
}}
.atrito-tag {{
  position: absolute;
  top: -22px;
  right: -6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--atrevo);
  white-space: nowrap;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
}}

/* blocos de seção */
.block {{
  position: relative;
  margin-bottom: 44px;
  opacity: 0;
  transform: translateY(22px);
  transition: opacity 700ms cubic-bezier(.2,.7,.2,1), transform 700ms cubic-bezier(.2,.7,.2,1);
}}
.block.in {{ opacity: 1; transform: translateY(0); }}

.block .tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 14px;
}}
.block .tag::before {{
  content: ""; width: 7px; height: 7px; border-radius: 2px;
}}
.block[data-kind="cenario"]   .tag {{ color: var(--tinta-soft); }}
.block[data-kind="cenario"]   .tag::before {{ background: var(--tinta-soft); }}
.block[data-kind="dor"]       .tag {{ color: var(--atrevo); }}
.block[data-kind="dor"]       .tag::before {{ background: var(--atrevo); }}
.block[data-kind="causa"]     .tag {{ color: var(--tinta-soft); }}
.block[data-kind="causa"]     .tag::before {{ background: var(--tinta-soft); opacity:.5; }}
.block[data-kind="cerebro"]   .tag {{ color: var(--realce); }}
.block[data-kind="cerebro"]   .tag::before {{ background: var(--realce); }}
.block[data-kind="solucao"]   .tag {{ color: var(--leve); }}
.block[data-kind="solucao"]   .tag::before {{ background: var(--leve); }}
.block[data-kind="exercicio"] .tag {{ color: var(--leve); }}
.block[data-kind="exercicio"] .tag::before {{ background: var(--leve); }}
.block[data-kind="resumo"]    .tag {{ color: var(--tinta); }}
.block[data-kind="resumo"]    .tag::before {{ background: var(--tinta); }}
.block[data-kind="transicao"] .tag {{ color: var(--realce); }}
.block[data-kind="transicao"] .tag::before {{ background: var(--realce); }}
.block[data-kind="pagina"]    .tag {{ color: var(--atrevo); }}
.block[data-kind="pagina"]    .tag::before {{ background: var(--atrevo); }}

.block h3 {{
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -0.015em;
  margin-bottom: 14px;
}}
.block p, .block ul, .block ol, .block blockquote {{
  font-size: 18px;
  color: var(--tinta);
}}
.block ul, .block ol {{ padding-left: 22px; margin: 0 0 1.1em; }}
.block li {{ margin-bottom: 8px; }}

.block blockquote {{
  margin: 18px 0;
  padding: 16px 20px;
  border-left: 3px solid var(--leve);
  background: var(--leve-soft);
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 19px;
  color: var(--tinta);
  border-radius: 0 8px 8px 0;
}}

/* cartões especiais */
.block[data-kind="cerebro"] {{
  background: var(--papel-2);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 26px 28px;
  box-shadow: var(--shadow);
}}
.block[data-kind="cerebro"]::after {{
  content: "caderno de campo";
  position: absolute;
  top: 14px; right: 18px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--realce);
  opacity: .7;
}}

.block[data-kind="exercicio"] {{
  background: #FFFDF6;
  border: 1px dashed var(--leve);
  border-radius: 12px;
  padding: 28px 28px 22px;
  position: relative;
}}
.block[data-kind="exercicio"]::before {{
  content: "";
  position: absolute;
  top: -10px; left: 28px;
  width: 54px; height: 18px;
  background: rgba(62, 123, 107, 0.18);
  transform: rotate(-2deg);
  border-radius: 2px;
}}

.block[data-kind="resumo"] {{
  border-top: 1px solid var(--line-2);
  padding-top: 22px;
}}
.block[data-kind="resumo"] ul {{
  list-style: none;
  padding-left: 0;
}}
.block[data-kind="resumo"] li {{
  padding-left: 22px;
  position: relative;
  margin-bottom: 10px;
}}
.block[data-kind="resumo"] li::before {{
  content: "→";
  position: absolute; left: 0; top: 0;
  color: var(--leve);
  font-weight: 700;
}}

.block[data-kind="transicao"] {{
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 19px;
  color: var(--tinta-soft);
  border-top: 1px solid var(--line);
  padding-top: 28px;
  margin-top: 12px;
}}

/* parte prática (capítulo 31) */
.chapter.parte .chapter-head h2 {{
  color: var(--atrevo);
}}
.chapter.parte .block[data-kind="pagina"] {{
  background: var(--papel-2);
  border-radius: 12px;
  padding: 24px 26px;
  border: 1px solid var(--line);
}}
.chapter.parte .block[data-kind="pagina"] h3 {{
  color: var(--atrevo);
}}

/* rodapé */
.foot {{
  max-width: 720px;
  margin: 120px auto 0;
  padding: 60px 56px 80px;
  text-align: center;
  border-top: 1px solid var(--line);
}}
.foot .end {{
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 26px;
  color: var(--leve);
  margin-bottom: 10px;
}}
.foot .end-sub {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--tinta-soft);
}}
.foot a.back {{
  display: inline-block;
  margin-top: 28px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--tinta);
  border: 1px solid var(--line-2);
  padding: 12px 20px;
  border-radius: 999px;
  transition: background .2s, border-color .2s;
}}
.foot a.back:hover {{ background: var(--papel-2); border-color: var(--atrevo); }}

/* menu mobile */
.rail-toggle {{
  display: none;
  position: fixed;
  top: 16px; left: 16px;
  z-index: 40;
  background: var(--papel-2);
  border: 1px solid var(--line-2);
  border-radius: 10px;
  padding: 10px 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--tinta);
  cursor: pointer;
  box-shadow: var(--shadow);
}}
.scrim {{
  display: none;
  position: fixed; inset: 0;
  background: rgba(27,26,23,0.4);
  z-index: 25;
  opacity: 0;
  transition: opacity .25s;
}}

/* ---------- responsivo ---------- */
@media (max-width: 980px) {{
  .rail {{
    transform: translateX(-100%);
    transition: transform .3s cubic-bezier(.2,.7,.2,1);
    box-shadow: var(--shadow);
  }}
  .rail.open {{ transform: translateX(0); }}
  .rail-toggle {{ display: inline-flex; }}
  .reader {{ margin-left: 0; }}
  .reader > * {{ padding-left: 24px; padding-right: 24px; }}
  .atrito {{ right: 8px; }}
  .scrim.show {{ display: block; opacity: 1; }}
  body.rail-open {{ overflow: hidden; }}
}}
@media (max-width: 560px) {{
  body {{ font-size: 17px; }}
  .cover {{ padding-top: 100px; }}
  .block[data-kind="cerebro"]::after {{ display: none; }}
  .atrito, .atrito-tag {{ display: none; }}
  .reader > * {{ padding-left: 20px; padding-right: 20px; }}
}}

@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }}
  .block {{ opacity: 1; transform: none; }}
  .cover .seal, .cover h1, .cover .sub, .cover .meta, .scroll-cue {{ opacity: 1; transform: none; animation: none; }}
  .atrito-fill {{ transform: translateY(0); }}
  html {{ scroll-behavior: auto; }}
}}
</style>
</head>
<body>

<button class="rail-toggle" id="railToggle" aria-label="Abrir índice">Índice</button>
<div class="scrim" id="scrim"></div>

<aside class="rail" id="rail">
  <div class="brand">Rotina <span class="light">Leve</span></div>
  <div class="brand-sub">Playbook Animado</div>
  <div class="progress-label"><span>Progresso</span><span id="pct">0%</span></div>
  <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
  <div class="toc-title">Capítulos</div>
  <ol id="toc">
{toc_items}
  </ol>
</aside>

<main class="reader">

<section class="cover" id="cover">
  <span class="seal">Playbook Animado · Edição de Leitura</span>
  <h1>Rotina <span class="light">Leve</span></h1>
  <p class="sub">O método anti-procrastinação para mentes aceleradas — uma experiência de leitura que drena o atrito conforme você avança.</p>
  <div class="meta">
    <span><i class="dot"></i> 31 capítulos</span>
    <span><i class="dot leve"></i> do atrito à leveza</span>
    <span>7 dias · método prático</span>
  </div>
  <span class="scroll-cue">Role para começar</span>
</section>

{chapters_html}

<footer class="foot">
  <div class="end">Uma rotina leve não é uma rotina perfeita. É uma rotina possível.</div>
  <div class="end-sub">Fim do playbook</div>
  <a class="back" href="../">Voltar para a página inicial</a>
</footer>

</main>

<script>
(function () {{
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // reveal dos blocos
  const blocks = document.querySelectorAll('.block');
  if (reduce) {{
    blocks.forEach(b => b.classList.add('in'));
  }} else {{
    const io = new IntersectionObserver((entries) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{
          e.target.classList.add('in');
          io.unobserve(e.target);
        }}
      }});
    }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.12 }});
    blocks.forEach(b => io.observe(b));
  }}

  // medidor de atrito por capítulo (scroll-linked)
  const chapters = [...document.querySelectorAll('.chapter')];
  const fills = new Map();
  chapters.forEach(ch => {{
    const fill = ch.querySelector('.atrito-fill');
    if (fill) fills.set(ch, fill);
  }});

  function updateAtrito() {{
    const vh = window.innerHeight;
    chapters.forEach(ch => {{
      const fill = fills.get(ch);
      if (!fill) return;
      const r = ch.getBoundingClientRect();
      const start = r.top - vh * 0.7;
      const end = r.bottom - vh * 0.5;
      const span = end - start;
      let p = (0 - start) / span;
      p = Math.max(0, Math.min(1, p));
      // fill sobe de translateY(100%) -> 0 conforme avança (drena o atrito, revela a leveza)
      fill.style.transform = 'translateY(' + ((1 - p) * 100) + '%)';
    }});
  }}

  // progresso global + capítulo ativo no índice
  const tocLinks = [...document.querySelectorAll('#toc a')];
  const progressFill = document.getElementById('progressFill');
  const pctEl = document.getElementById('pct');
  const cover = document.getElementById('cover');

  function updateProgress() {{
    const max = document.body.scrollHeight - window.innerHeight;
    const sc = window.scrollY;
    const p = max > 0 ? sc / max : 0;
    progressFill.style.width = (p * 100) + '%';
    pctEl.textContent = Math.round(p * 100) + '%';

    // capítulo ativo: o último cujo topo passou do terço superior
    const probe = window.innerHeight * 0.35;
    let active = null;
    for (const ch of chapters) {{
      if (ch.getBoundingClientRect().top - probe <= 0) active = ch;
    }}
    tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + (active ? active.id : 'cover')));
  }}

  let ticking = false;
  function onScroll() {{
    if (!ticking) {{
      ticking = true;
      requestAnimationFrame(() => {{
        updateAtrito();
        updateProgress();
        ticking = false;
      }});
    }}
  }}
  window.addEventListener('scroll', onScroll, {{ passive: true }});
  window.addEventListener('resize', onScroll);
  updateAtrito();
  updateProgress();

  // índice mobile
  const rail = document.getElementById('rail');
  const toggle = document.getElementById('railToggle');
  const scrim = document.getElementById('scrim');
  function closeRail() {{
    rail.classList.remove('open');
    scrim.classList.remove('show');
    document.body.classList.remove('rail-open');
  }}
  toggle.addEventListener('click', () => {{
    const open = rail.classList.toggle('open');
    scrim.classList.toggle('show', open);
    document.body.classList.toggle('rail-open', open);
  }});
  scrim.addEventListener('click', closeRail);
  tocLinks.forEach(a => a.addEventListener('click', () => {{
    if (window.matchMedia('(max-width: 980px)').matches) closeRail();
  }}));
}})();
</script>
</body>
</html>
"""


def render_chapter(ch: dict) -> str:
    is_parte = ch["is_parte"]
    cls = "chapter parte" if is_parte else "chapter"
    num = ch["num"]
    num_label = f"{num:02d}"
    head = f'''
<article class="{cls}" id="ch-{num}">
  <div class="chapter-head">
    <span class="num">Capítulo {num_label} <span class="of">/ 31</span></span>
    <h2>{html.escape(ch["title"])}</h2>
    <div class="num-line"></div>
  </div>
  <div class="atrito" aria-hidden="true">
    <span class="atrito-tag">Atrito → Leveza</span>
    <div class="atrito-fill"></div>
  </div>'''

    blocks = []
    for s in ch["sections"]:
        label = KIND_LABEL.get(s["kind"], "Texto")
        blocks.append(f'''
  <section class="block" data-kind="{s["kind"]}">
    <span class="tag">{label}</span>
    <h3>{html.escape(s["title"])}</h3>
    {s["body"]}
  </section>''')

    # para a parte prática, o título "Capítulo 31 / 31" não faz sentido; ajusta
    if is_parte:
        head = f'''
<article class="{cls}" id="ch-{num}">
  <div class="chapter-head">
    <span class="num">Parte 2 <span class="of">· Prático</span></span>
    <h2>{html.escape(ch["title"])}</h2>
    <div class="num-line"></div>
  </div>'''

    return head + "\n" + "\n".join(blocks) + "\n</article>"


def render_toc(chapters: list[dict]) -> str:
    items = []
    for ch in chapters:
        num = ch["num"]
        # título curto para o índice: remove prefixo "Capítulo N:" e "PARTE 2:"
        t = ch["title"]
        t = re.sub(r"^Cap[íi]tulo\s+\d+:\s*", "", t, flags=re.I)
        t = re.sub(r"^Parte\s+\d+:\s*", "", t, flags=re.I)
        if len(t) > 46:
            t = t[:44].rstrip() + "…"
        label = f"{num:02d}" if not ch["is_parte"] else "P2"
        items.append(
            f'    <li><a href="#ch-{num}"><span class="n">{label}</span><span>{html.escape(t)}</span></a></li>'
        )
    return "\n".join(items)


def build():
    chapters = load_chapters()
    toc = render_toc(chapters)
    chapters_html = "\n\n".join(render_chapter(c) for c in chapters)
    html_out = TEMPLATE.format(toc_items=toc, chapters_html=chapters_html)

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_out)

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"Playbook animado gerado: {OUTPUT}")
    print(f"Capítulos: {len(chapters)} | Tamanho: {size_kb:.1f} KB")


if __name__ == "__main__":
    build()