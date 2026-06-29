# Rotina Leve — Playbook Anti-Procrastinação

Produto digital em formato de playbook prático para pessoas com mente acelerada que querem começar tarefas, reduzir atrito e organizar a rotina sem depender só de força de vontade.

## Produto

**Nome:** Rotina Leve  
**Subtítulo:** Playbook Anti-Procrastinação para Mentes Aceleradas  
**Formato:** PDF + checklist + planner + landing page  
**Preço inicial sugerido:** R$ 37 a R$ 47  
**Upsell sugerido:** Mini curso em áudio de 7 dias

## Promessa

Transforme tarefas confusas em pequenas ações possíveis usando um método simples de 7 dias.

## Landing page (v2 — visual premium)

A landing em `landing/index.html` é uma página de vendas completa, responsiva e self-contained (sem dependências de build). Inclui:

- Nav sticky + hero com mockup da capa e gradient
- Seção "Para quem é" (4 personas)
- Método Rotina Leve (5 passos) e "O que você recebe" (6 entregáveis)
- Plano de 7 dias
- Card de preço com order bump (R$ 17) e upsell (R$ 97)
- Selo de garantia de 7 dias, FAQ e CTA final
- Footer com disclaimer (material educativo, não substitui avaliação profissional)
- Animações reveal-on-scroll, fontes Inter/Sora via Google Fonts

### Rodar localmente

```bash
cd rotina-leve-playbook
python -m http.server 8000
```

Abra:

```text
http://localhost:8000/landing
```

### Publicar (GitHub Pages)

```bash
gh repo create rotina-leve-playbook --public --description "Playbook anti-procrastinação para mentes aceleradas"
# após o push, ative o Pages apontando para a branch main / pasta /landing
```

## Estrutura

```text
content/              Conteúdo do playbook e bônus (markdown)
landing/              Página de venda HTML (v2 premium)
prompts/              Prompts para gerar criativos, páginas e versões do produto
scripts/              Notas para exportação futura (PDF/EPUB)
PRODUCT_STRATEGY.md   Estratégia, público, oferta e riscos de copy
package.json          Metadados do projeto
```

## Antes de publicar (checklist)

1. Revisar o playbook em `content/playbook.md`
2. Trocar `https://pay.cakto.com.br/SEU-LINK-AQUI` pela URL real de checkout
3. Trocar `suporte@rotinaleve.com` pelo e-mail de atendimento real
4. Gerar capa 3:4 premium e mockups para o hero
5. (Opcional) Ativar GitHub Pages apontando para `/landing`
