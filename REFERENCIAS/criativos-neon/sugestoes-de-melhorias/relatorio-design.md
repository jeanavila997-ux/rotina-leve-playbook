# Relatório de Design — TDAH Descomplicado

## 1. Resumo executivo

A landing page do **TDAH Descomplicado** já possui uma identidade visual limpa e um funil de vendas funcional, mas apresenta **bugs de classe Tailwind, problemas de acessibilidade críticos e sobrecarga de movimento** que prejudicam usuários neurodivergentes e reduzem a confiança na compra. Este relatório prioriza correções de baixo esforço e alto impacto para alinhar a experiência ao design system Soft Light e às boas práticas de neuroacessibilidade.

---

## 2. O que está funcionando

- **Proposta de valor clara:** o e-book + bônus são comunicados de forma direta na hero section.
- **Evidência social:** depoimentos e notificações de compra reforçam a decisão.
- **Interatividade:** checklist dopamina, quiz, timer de foco e leitura bionic incentivam engajamento.
- **Paleta base forte:** Soft Light (`#FAFBFD`, `#4F46E5`, `#0EA5E9`, `#F43F5E`) já documentada no design system.

---

## 3. Problemas críticos (P0)

### 3.1 Classes Tailwind inválidas

Várias classes digitadas incorretamente não produzem nenhum efeito visual, quebrando layout ou z-index em produção:

| Classe inválida | Ocorrência | Correção |
| --- | --- | --- |
| `justify-content-center` | Hero, quiz | `justify-center` |
| `z-9999` / `z-999` / `z-99` | Dock flutuante, progress bar, modais | `z-50`, `z-40`, `z-30` |
| `rounded-t-[24px]` (ok) | — | usar token `rounded-3xl` ou `--radius-3xl` |

**Impacto:** elementos podem ficar desalinhados ou sobrepostos de forma imprevisível em telas pequenas.

### 3.2 Acessibilidade e interação

- **Acordeões e checklists customizados** usam `<div onClick>` sem `role`, `tabIndex` nem suporte à tecla `Enter`/`Space`.
- **Não há região `aria-live`** para anúncios do timer, quiz e notificações de compra.
- **Toques pequenos:** ícones e links do dock podem ter área inferior a 44×44 px.
- **Áudio autoplay** dispara sem consentimento do usuário, violando princípios de WCAG e causando distração em ADHD.
- **Notificações de urgência fake** em loop aumentam ansiedade e reduzem credibilidade.

### 3.3 Modal de checkout abandonado

`src/components/CheckoutModal.tsx` está referenciado mas **não é usado** no fluxo atual. Ele contém:

- classes Tailwind inválidas;
- semântica de diálogo ausente (`<dialog>` ou `role="dialog"`);
- contador falso de escassez;
- validação fraca de campos.

**Recomendação:** ou remove-lo ou refatorá-lo com `shadcn/ui Dialog` + validação real.

### 3.4 Divergência do design system

- CTA primário ao vivo usa **sky blue (`#0EA5E9`)**, enquanto o design system aponta **indigo (`#4F46E5`)**.
- Tipografia usa **Geist Variable**; o design system cita Roboto/Inter.
- A sobreposição de cor dificulta a padronização de novos criativos (neon vs. soft light).

---

## 4. Oportunidades de melhoria (P1/P2)

### 4.1 Design

- Criar **tokens de espaçamento e tipografia consistentes** no `@theme` do Tailwind v4.
- Adotar **border-radius e sombras** do design system em todos os cards e botões.
- Melhorar hierarquia de leitura na hero: tamanho de título, subtítulo e preço em proporção clara.
- Introduzir **feedback visual em todos os estados** dos componentes interativos.

### 4.2 Acessibilidade / Neuroacessibilidade (ADHD)

- Implementar `prefers-reduced-motion` e respeitá-lo globalmente.
- Substituir notificações de urgência por **prova social real** (número real de vendas do dia, depoimentos).
- Aumentar áreas de toque para ≥ 44×44 px.
- Adicionar `skip-link` para navegação por teclado.
- Tornar todos os componentes interativos focáveis e anunciáveis por leitor de tela.

### 4.3 Performance e conversão

- Remover áudio autoplay ou substituir por player com controle explícito.
- Lazy-load imagens fora da viewport.
- Otimizar o LCP da hero (imagem + texto + CTA).
- A/B testar cor do CTA primário (indigo vs. sky blue) com base em conversão, não só na paleta.

### 4.4 Motion (Hyperframes/Framer Motion)

- Substituir pulsações contínuas por **animações de entrada suaves e paradas**.
- Usar `AnimatePresence` para transições de seção (quiz, resultados).
- Adicionar **microfeedback** ao marcar itens dos checklists (ícone + cor + vibração sutil).
- Criar **stagger leve** nos depoimentos, evitando movimento simultâneo.

---

## 5. Métricas de sucesso sugeridas

- **Conversão:** taxa de cliques no botão de compra (Cakto).
- **Engajamento:** taxa de conclusão do quiz, itens marcados no checklist, tempo no timer.
- **Acessibilidade:** 0 erros no Lighthouse/axe-core; navegação 100% por teclado.
- **Performance:** LCP < 2,5 s; CLS < 0,1; INP < 200 ms.

---

## 6. Próximos passos imediatos

1. Corrigir classes Tailwind inválidas (`relatorio-design.md` §3.1).
2. Remover/reativar modal de checkout com acessibilidade.
3. Implementar `prefers-reduced-motion` e regiões `aria-live`.
4. Validar contraste e tamanho de toque.
5. Executar o checklist em [`checklist-acessibilidade.md`](./checklist-acessibilidade.md).

Veja detalhes de implementação e priorização em [`plano-de-acao-p0-p1-p2.md`](./plano-de-acao-p0-p1-p2.md).

---

*Relatório gerado em 2026-06-29 com base na auditoria do repositório `jeanavila997-ux/tdah-descomplicado`.*
