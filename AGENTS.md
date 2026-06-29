# Repository Guidelines

## Project Overview
**Rotina Leve** is a premium digital product (Playbook) designed to help students, developers, and creators overcome procrastination and optimize their routines. The project focuses on a practical, non-clinical, and "guilt-free" approach to productivity.

## Architecture & Data Flow
The project follows a **Source → Build → Product → Sales** pipeline.

### Content Pipeline
`content/playbook/*.md` (Numbered Chapters) 
$\rightarrow$ `scripts/compile.py` (Aggregation) 
$\rightarrow$ `content/playbook.md` (Compiled Markdown) 
$\rightarrow$ `scripts/export_pdf.py` (Playwright Rendering) 
$\rightarrow$ `content/rotina-leve-playbook.pdf` (Final Product)

### Sales Pipeline
`PRODUCT_STRATEGY.md` (Strategy) 
$\rightarrow$ `content/landing-copy.md` (Copywriting) 
$\rightarrow$ `landing/index.html` (Static Sales Page) 
$\rightarrow$ Cakto Checkout $\rightarrow$ `landing/obrigado.html` (Post-Purchase)

## Key Directories
- `content/`: Core product IP. Contains source chapters (`playbook/`), the compiled markdown, the final PDF, and marketing copy.
- `landing/`: The conversion layer. Contains the self-contained sales page and assets.
- `scripts/`: Python-based automation for content compilation and PDF generation.
- `prompts/`: AI orchestration layer. Defines agent personas (e.g., Product Builder) and creative factories.
- `skills/`: Specialist AI knowledge bases (e.g., Frontend Design, Code Reviewer) used to guide implementation.
- `REFERENCIAS/`: A read-only mirror of external design systems (Open Design) and reference materials.

## Development Commands

### Environment Setup
```bash
# Activate Python virtual environment
. .venv\Scripts\Activate.ps1
```

### Content Build
```bash
# 1. Consolidate chapters into a single markdown file
python scripts/compile.py

# 2. Render the consolidated markdown into a styled PDF
python scripts/export_pdf.py
```

### Landing Page Preview
```bash
# Start a local server
python -m http.server 8000
# Access at: http://localhost:8000/landing/
```

## Code Conventions & Common Patterns
- **Language & Tone**: Portuguese (Brazil). The voice is light, practical, and encouraging. **NEVER** use medical framing, diagnose, or promise "cures."
- **Chapter Structure**: Source chapters follow a specific flow: `Real Scenario → Pain → Cause → Simple Brain Science → Practical Solution → Practical Exercise → Summary → Transition`.
- **Naming Convention**: Chapters in `content/playbook/` must be zero-padded (e.g., `01_intro.md`, `02_topic.md`) for natural sorting by the compiler.
- **Web Development**: The landing page is a **single, self-contained HTML file** with inline CSS/JS to maximize portability and loading speed.

## Important Files
- `README.md`: The project map, quick-start guide, and pre-publish checklist.
- `PRODUCT_STRATEGY.md`: The "Source of Truth" for audience, positioning, and offer structure.
- `PROXIMOS_PASSOS.md`: The active operational backlog and go-to-market tracker.
- `.session-context.md`: Technical session state, including environment details and immediate priorities.

## Runtime & Tooling
- **Primary Runtime**: Python 3.x.
- **Key Dependencies**: `markdown` (for HTML conversion), `playwright` (for PDF rendering via headless Chromium).
- **Web Hosting**: Designed for static hosting (e.g., GitHub Pages, Vercel, Netlify).

## Testing & QA
- **PDF Validation**: Manual review of `content/rotina-leve-playbook.pdf` after running the build scripts to ensure typography and page breaks are correct.
- **Landing Page QA**: Test responsiveness across mobile and desktop viewports. Verify all CTA links point to the correct checkout/support endpoints.
