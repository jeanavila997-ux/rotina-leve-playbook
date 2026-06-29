# Plano de Ação P0 → P1 → P2 — TDAH Descomplicado

Roadmap prático de melhorias dividido em três camadas de prioridade:

- **P0 — Blockers:** bugs que quebram layout, acessibilidade ou confiança. Devem ser corrigidos antes de qualquer novo recurso.
- **P1 — Ganhos rápidos:** baixo esforço, alto impacto em conversão e experiência.
- **P2 — Consolidação:** refinamentos que exigem mais testes e decisões de produto.

---

## P0 — Blockers (corrigir na próxima sprint)

| # | Tarefa | Onde | Como fazer | Critério de pronto |
| --- | --- | --- | --- | --- |
| P0.1 | Corrigir classes Tailwind inválidas | `src/App.tsx`, componentes | Substituir `justify-content-center` por `justify-center`; `z-9999/999/99` por `z-50/40/30` | Build passa; layout estável em mobile e desktop |
| P0.2 | Remover ou refatorar `CheckoutModal.tsx` | `src/components/CheckoutModal.tsx` | Se mantido: usar `Dialog` do shadcn, validar campos, sem countdown fake; se removido: limpar imports e referências | Não há componente inativo; CTA redireciona corretamente para Cakto |
| P0.3 | Tornar checklists acessíveis por teclado | `DopamineChecklist.tsx`, `WinsChecklist.tsx` | Converter linhas `<div onClick>` em `<button>` ou `<label>+<input type="checkbox">` | Navegação 100% via Tab/Enter/Space; axe-core sem erros |
| P0.4 | Desativar autoplay de áudio | `src/App.tsx` | Remover `autoPlay`; exibir player com play explícito | Lighthouse não reporta autoplay; usuário controla som |
| P0.5 | Respeitar `prefers-reduced-motion` | `src/index.css`, componentes | Adicionar `@media (prefers-reduced-motion: reduce)` desabilitando `animate-calm-pulse`, pulsações e toast | Redução de motion ativada no OS reflete na página |
| P0.6 | Adicionar regiões `aria-live` | `AutoFocusTimer`, `AdhdQuiz`, notificações | Envelopar estados dinâmicos em `<div aria-live="polite" aria-atomic="true">` | NVDA/VoiceOver anuncia timer/quiz/resultados |

---

## P1 — Ganhos rápidos (1–2 semanas)

| # | Tarefa | Onde | Como fazer | Critério de pronto |
| --- | --- | --- | --- | --- |
| P1.1 | Alinhar CTA primário ao design system | `src/App.tsx`, `src/index.css` | Testar indigo (`#4F46E5`) como CTA principal e manter sky blue como hover/accent se quiser | Paleta documentada aplicada; A/B test configurado |
| P1.2 | Padronizar tokens de tipografia e espaçamento | `src/index.css` | Definir `--font-sans` único; criar `text-balance`, `leading-relaxed` para blocos longos | Sem conflito de fontes; hierarquia visual consistente |
| P1.3 | Melhorar toques e áreas de clique | Dock flutuante, ícones, CTAs | Aumentar `min-w`/`min-h` para 44–48 px; adicionar `p-2` nos botões do dock | Todos os alvos passam no teste de 44 px |
| P1.4 | Tornar acordeões semanticamente corretos | FAQ e currículo | Usar `details`/`summary` ou `Accordion` do shadcn com `aria-expanded` | Navegação por teclado funciona; leitor de tela anuncia estado |
| P1.5 | Implementar `skip-link` | `src/App.tsx` | Link invisível que aparece no `Tab` e leva ao `<main>` | Teste de teclado passa |
| P1.6 | Reescrever notificações de urgência | Toast de compras | Substituir loop automático por dados reais ou removê-lo | Sem "urgência falsa"; notificações opcionais |

---

## P2 — Consolidação (próximas 4–6 semanas)

| # | Tarefa | Onde | Como fazer | Critério de pronto |
| --- | --- | --- | --- | --- |
| P2.1 | Refatorar `App.tsx` em seções componentizadas | `src/App.tsx` | Extrair Hero, Benefits, Curriculum, Testimonials, FAQ, FinalCTA em arquivos menores | Cada seção testável isoladamente |
| P2.2 | Criar biblioteca de microanimações acessíveis | `src/index.css` + componentes | Definir tokens `animate-fade-in`, `animate-slide-up` e variação `prefers-reduced-motion` | Motion consistente e respeita redução |
| P2.3 | Otimizar performance da hero | Imagens, fontes, scripts | Lazy load fora da viewport; preload fonte e imagem LCP; reduzir JS não crítico | Lighthouse LCP < 2,5 s; CLS < 0,1 |
| P2.4 | Testes de usabilidade com usuários reais | — | Recrutar 3 usuários com TDAH para tarefas de descoberta de preço, quiz e compra | Relatório de findings e ajustes |
| P2.5 | Implementar lead-magnet por e-mail | Hero ou seção de bônus | Formulário simples com label, validação e integração (Cakto/lista) | Captura funcional; taxa de conversão medida |
| P2.6 | Documentar design system atualizado | `criativos-soft-light/assets/design-system.md` | Atualizar cores, tipografia, componentes e tokens do Tailwind v4 | Designers e devs usam mesma fonte de verdade |

---

## Ordem sugerida de execução

```text
Semana 1: P0.1 → P0.2 → P0.3 → P0.4 → P0.5 → P0.6
Semana 2: P1.1 → P1.2 → P1.3 → P1.4 → P1.5 → P1.6
Semana 3+: P2.1 → P2.2 → P2.3 → P2.4 → P2.5 → P2.6
```

---

## Métricas de acompanhamento

| Métrica | Baseline | Meta P0+P1 | Meta P2 |
| --- | --- | --- | --- |
| Lighthouse Accessibility | ~? | ≥ 90 | 100 |
| Lighthouse Performance | ~? | ≥ 70 | ≥ 85 |
| Taxa de clique no CTA | — | +10% | +20% |
| Conclusão do quiz | — | +15% | +25% |
| Reclamações de distração | — | 0 | 0 |

---

*Plano gerado em 2026-06-29. Acompanhar progresso no README e no checklist de acessibilidade.*
