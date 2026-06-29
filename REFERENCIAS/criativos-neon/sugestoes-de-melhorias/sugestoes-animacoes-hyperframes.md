# Sugestões de Animações com Hyperframes/Framer Motion — TDAH Descomplicado

Este documento propõe microanimações e transições para reduzir fricção cognitiva, reforçar feedback e manter a experiência acessível a pessoas com TDAH. As sugestões usam a API `motion` (Framer Motion v12) já presente no projeto, mas podem ser adaptadas para Hyperframes ou CSS puro com `prefers-reduced-motion`.

---

## Princípios de motion para ADHD

1. **Motion com propósito:** cada animação deve guiar atenção, confirmar ação ou revelar progresso.
2. **Curta duração:** preferencialmente 200–350 ms.
3. **Redução respeitada:** se `prefers-reduced-motion: reduce`, transformações são instantâneas ou ausentes.
4. **Evitar pulsação contínua:** animações em loop devem ser sutis, pausáveis e limitadas.
5. **Stagger moderado:** revelar elementos aos poucos, nunca tudo ao mesmo tempo.

---

## 1. Hero section — entrada suave e hierarquia

### Problema atual
Texto e CTA podem aparecer de forma abrupta; a pulsação do badge de urgência compete com a atenção do título.

### Sugestão
```tsx
import { motion } from "motion/react";

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

<motion.div
  initial={{ opacity: 0, y: reducedMotion ? 0 : 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.4, ease: "easeOut" }}
>
  <h1>Domine seu TDAH com estratégias práticas</h1>
</motion.div>
```

- **Badge:** remover pulsação infinita; usar `whileHover` leve ou fade único ao carregar.
- **CTA:** `whileHover={{ scale: 1.03 }}` + `whileTap={{ scale: 0.98 }}` (respeitado por `prefers-reduced-motion`).

---

## 2. Checklists — microfeedback ao marcar

### Problema atual
Linhas são `<div onClick>`, sem feedback visual acessível.

### Sugestão
```tsx
<motion.button
  whileTap={{ scale: 0.97 }}
  animate={checked ? { backgroundColor: "#ECFDF5" } : { backgroundColor: "#FFFFFF" }}
  transition={{ duration: 0.2 }}
  aria-pressed={checked}
>
  <motion.span animate={{ scale: checked ? 1.2 : 1, rotate: checked ? 0 : -10 }}>✓</motion.span>
  {label}
</motion.button>
```

- Marcar um item dispara **ícone crescendo + cor de sucesso**.
- Anunciar estado para leitor de tela com `aria-live="polite"`.

---

## 3. Quiz — transições de pergunta

### Problema atual
Transições de pergunta não são claras; progresso não é anunciado.

### Sugestão
```tsx
<AnimatePresence mode="wait">
  <motion.div
    key={currentQuestion}
    initial={{ opacity: 0, x: reducedMotion ? 0 : 20 }}
    animate={{ opacity: 1, x: 0 }}
    exit={{ opacity: 0, x: reducedMotion ? 0 : -20 }}
    transition={{ duration: 0.25 }}
  >
    ...pergunta...
  </motion.div>
</AnimatePresence>
```

- Barra de progresso com `role="progressbar"`, `aria-valuenow` e transição de largura suave.
- Resultado final aparece com `fade + scale` e `aria-live="polite"`.

---

## 4. Timer de foco — estado por cor e animação

### Problema atual
Timer não comunica mudanças de estado para quem não enxerga a tela.

### Sugestão
```tsx
const ringVariants = {
  idle: { stroke: "#94A3B8" },
  running: { stroke: "#4F46E5" },
  done: { stroke: "#10B981", scale: reducedMotion ? 1 : 1.05 }
};

<motion.div
  variants={ringVariants}
  animate={timerState}
  transition={{ duration: 0.3 }}
  aria-live="polite"
>
  {formatTime(timeLeft)}
</motion.div>
```

- Quando termina, anunciar "Tempo de foco concluído".
- Evitar vibração/pulsação contínua; fazer um único pulse ao finalizar.

---

## 5. Depoimentos e prova social — stagger leve

### Problema atual
Muitos elementos podem entrar juntos, sobrecarregando a atenção.

### Sugestão
```tsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
};

const item = {
  hidden: { opacity: 0, y: reducedMotion ? 0 : 16 },
  show: { opacity: 1, y: 0, transition: { duration: 0.3 } }
};

<motion.div variants={container} initial="hidden" whileInView="show" viewport={{ once: true }}>
  {testimonials.map(t => (
    <motion.div key={t.id} variants={item}>...</motion.div>
  ))}
</motion.div>
```

- `whileInView="show"` dispara apenas uma vez (`viewport={{ once: true }}`).
- Notificações de compra em fade único, **não em loop**.

---

## 6. FAQ/Currículo — acordeão com semântica

### Problema atual
Acordeões não têm ARIA e animação brusca.

### Sugestão
```tsx
<motion.details
  initial={{ opacity: 0 }}
  whileInView={{ opacity: 1 }}
  viewport={{ once: true }}
  className="group"
>
  <summary className="cursor-pointer list-none">{título}</summary>
  <motion.div
    initial={false}
    animate={{ height: open ? "auto" : 0, opacity: open ? 1 : 0 }}
    transition={{ duration: 0.25 }}
  >{conteúdo}</motion.div>
</motion.details>
```

- Preferir elemento nativo `details`/`summary` para acessibilidade.
- Se usar componente customizado, adicionar `role="button"`, `aria-expanded`, `aria-controls`.

---

## 7. CTA flutuante/dock — estado ativo

### Problema atual
Dock pode ter z-index conflitante e áreas de toque pequenas.

### Sugestão
```tsx
<motion.nav
  className="fixed bottom-4 left-1/2 z-50 ..."
  initial={{ y: 100, opacity: 0 }}
  animate={{ y: 0, opacity: 1 }}
  transition={{ duration: 0.4, delay: 0.5 }}
>
  <motion.a
    href="https://pay.cakto.com.br/9u9w6q4_940459"
    whileHover={{ y: -2 }}
    whileTap={{ scale: 0.96 }}
    className="min-h-[48px] min-w-[48px]"
  >
    Comprar agora
  </motion.a>
</motion.nav>
```

- Garantir `z-50` máximo; substituir `z-9999`.
- Dock aparece após scroll ou delay, não imediatamente bloqueando a hero.

---

## 8. Utility de `prefers-reduced-motion`

Adicionar no `src/index.css`:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

E no TS:

```ts
export const prefersReducedMotion = () =>
  typeof window !== "undefined" &&
  window.matchMedia("(prefers-reduced-motion: reduce)").matches;
```

---

## Resumo de implementação

| Componente | Animação | Objetivo | Acessível? |
| --- | --- | --- | --- |
| Hero | Fade + slide suave | Hierarquia visual | Sim, com reduced motion |
| Checklist | Scale + cor | Feedback de conquista | Sim, com `aria-pressed` |
| Quiz | Slide entre perguntas | Orientar progresso | Sim, com progressbar ARIA |
| Timer | Cor + pulse único | Sinalizar conclusão | Sim, com `aria-live` |
| Depoimentos | Stagger leve | Evitar sobrecarga | Sim, `viewport.once` |
| FAQ | Height accordion | Revelar conteúdo gradualmente | Sim, nativo `details` |
| Dock | Entrada suave + hover | CTA sempre disponível | Sim, toque ≥ 48 px |

---

*Sugestões geradas em 2026-06-29 para uso com Framer Motion / Hyperframes no projeto `tdah-descomplicado`.*
