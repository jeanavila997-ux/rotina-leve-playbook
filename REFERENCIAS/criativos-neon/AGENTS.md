# Repository Guidelines

## Project Overview
This repository contains a collection of high-fidelity marketing creative assets for the launch of the digital product **"TDAH Descomplicado"**. The goal is to provide a cohesive visual identity across landing pages, Meta Ads, Instagram Carousels, and Stories, alongside copy for email nurturing and video scripts.

## Architecture & Data Flow
The project uses a **Static Creative Asset Architecture**. There is no application runtime, no backend, and no build pipeline.
- **Structure**: Every visual deliverable is a standalone, self-contained `.html` file.
- **Styling**: CSS is embedded directly within each file using `<style>` blocks.
- **Data Flow**: None. All content is authored statically.
- **Interactivity**: Minimal and CSS-driven (hover states, `@keyframes`). The only functional JavaScript is a single `window.open` call for the checkout link on the landing page.

## Key Directories
The project is flat; most assets reside in the root directory.
- `/`: Contains all HTML deliverables, Markdown copy, and the project manifest.
- `novos templates/`: Contains extraneous files unrelated to this project (e.g., `revisao.md` regarding vLLM Ascend) and should be ignored during creative maintenance.

## Development Commands
There are **no automated build, test, or lint commands**. 
- **Preview**: Open any `.html` file directly in a modern web browser.
- **Export**: Use the browser's "Print to PDF" or take high-resolution screenshots to generate final assets.
- **Validation**: Manual visual review against the design tokens in `README.md`.

## Code Conventions & Common Patterns
### Visual Design System (Soft Light)
All files must adhere to the Soft Light palette and typography to maintain brand consistency:
- Colors: 
  - Primary: `#4F46E5` (Indigo)
  - Secondary: `#0EA5E9` (Sky Blue)
  - Accent: `#F43F5E` (Rose/Red)
  - Background: `#FAFBFD` (Soft White)
  - Surface: `#FFFFFF` (White)
  - Text: `#1E293B` (Deep Slate Gray)
- Typography: Loaded via Google Fonts (Roboto, STIX Two Text, Source Code Pro).
- Implementation: Replicated in each file via :root CSS variables:
  ```css
  :root {
    --neon-primary: #4F46E5;
    --neon-secondary: #0EA5E9;
    --neon-accent: #F43F5E;
    --neon-dark: #FAFBFD;
    --neon-surface: #FFFFFF;
    --neon-text: #1E293B;
  }
  ```

### HTML/CSS Patterns
- **Fixed Dimensions**: Ads and social assets use fixed containers (e.g., `1080px x 1350px`, `1080px x 1080px`, `1080px x 1920px`).
- **Naming**: Portuguese semantic class names (e.g., `.topo`, `.meio`, `.baixo`, `.hero-features`).
- **Layout**: Heavy use of CSS Grid and Flexbox for responsiveness (Landing Page) and precise alignment (Ads).
- **Export Optimization**: `@media print` rules are used to ensure clean PDF exports.

## Important Files
- `README.md`: The authoritative project manifest. Contains design tokens, target audience, and the full list of assets.
- `landing-page-neon.html`: The primary conversion asset (Sales Page).
- `perfil-cliente.html`: Reference for target personas and audience segments.
- `emails-lancamento.md`: Nurturing sequence copy.
- `scripts-video.md`: Production scripts for short-form video content.

## Runtime/Tooling Preferences
- **Runtime**: No runtime required. Browser-based rendering only.
- **Package Manager**: None.
- **Editor**: VS Code (minimal settings).
- **Dependencies**: Google Fonts (CDN).

## Testing & QA
QA is entirely **manual and visual**:
1. **Rendering**: Open HTML in a browser and verify layout at the intended dimensions.
2. **Export**: Validate that "Print to PDF" produces a high-quality, artifact-free document.
3. **Copy Review**: Ensure Portuguese language consistency and factual accuracy of the offer.
4. **Links**: Verify the Cakto checkout link is functional and correct.
