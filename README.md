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

## Rodar localmente

Este repositório começa simples, com uma landing page HTML estática.

```bash
cd rotina-leve-playbook
python -m http.server 3000
```

Abra:

```text
http://localhost:3000/landing
```

## Estrutura

```text
content/              Conteúdo do playbook e bônus
landing/              Página de venda HTML
prompts/              Prompts para gerar criativos, páginas e versões do produto
scripts/              Scripts futuros para exportar PDF/EPUB
assets/               Imagens, capas e mockups
```

## Próximo passo

1. Revisar o playbook em `content/playbook.md`
2. Editar o preço e checkout na landing page
3. Gerar capa e mockups
4. Criar repositório no GitHub
5. Publicar no GitHub Pages, Hostinger ou Vercel
