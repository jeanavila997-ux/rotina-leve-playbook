# Sugestões de Melhorias — TDAH Descomplicado

Esta pasta contém o **diagnóstico de design, acessibilidade e animação** para o projeto `tdah-descomplicado`, gerado a partir de uma auditoria do repositório original.

## Arquivos

| Arquivo | Para quem é | O que contém |
| --- | --- | --- |
| [`relatorio-design.md`](./relatorio-design.md) | Product Owner, designer, desenvolvedor | Diagnóstico executivo do design atual, problemas críticos e oportunidades de melhoria de conversão. |
| [`checklist-acessibilidade.md`](./checklist-acessibilidade.md) | QA, frontend, designer | Lista verificável de acessibilidade e neuroacessibilidade (ADHD) com critérios WCAG/COGA. |
| [`plano-de-acao-p0-p1-p2.md`](./plano-de-acao-p0-p1-p2.md) | Tech lead, gestor de projeto | Roadmap de implementação priorizado em P0 (blockers), P1 (ganho rápido) e P2 (consolidação). |
| [`sugestoes-animacoes-hyperframes.md`](./sugestoes-animacoes-hyperframes.md) | Motion designer, frontend | Sugestões de microanimações e transições com Hyperframes/Framer Motion para reduzir fricção cognitiva. |

## Contexto

- **Stack auditada:** React 19 + Vite 6 + TypeScript 5.8 + Tailwind CSS v4 + `motion` (Framer Motion v12).
- **Arquivo principal:** `src/App.tsx` (~867 linhas), página de vendas do e-book "TDAH Descomplicado".
- **Design system de referência:** `criativos-soft-light/assets/design-system.md` (paleta Soft Light).
- **Auditoria anterior:** [`analise-e-sugestoes.md`](./analise-e-sugestoes.md) (15 sugestões preexistentes). Os entregáveis desta pasta a complementam e priorizam.

## Como usar

1. Leia `relatorio-design.md` para entender o cenário geral.
2. Use `checklist-acessibilidade.md` para testes manuais e automáticos.
3. Aplique `plano-de-acao-p0-p1-p2.md` na próxima sprint.
4. Consulte `sugestoes-animacoes-hyperframes.md` ao implementar motion.

---

*Gerado em 2026-06-29 pela auditoria de design do Copilot CLI.*
