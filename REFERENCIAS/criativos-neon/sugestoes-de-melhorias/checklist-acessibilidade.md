# Checklist de Acessibilidade e Neuroacessibilidade — TDAH Descomplicado

Este checklist deve ser usado nos testes de QA da landing page. Prioriza critérios **WCAG 2.2**, boas práticas **COGA** (Cognitive Accessibility) e adaptações para pessoas com **TDAH**.

## Como usar

Marque cada item durante revisão manual ou automatizada. Registre evidências (screenshot, log do axe-core, vídeo de navegação por teclado).

---

## 1. Estrutura e navegação

- [ ] Existe `skip-link` visível ao pressionar `Tab` que leva ao conteúdo principal.
- [ ] A página possui hierarquia de títulos lógica (`h1` → `h2` → `h3`), sem saltos.
- [ ] Todos os landmarks (`header`, `main`, `section`, `footer`) estão semanticamente corretos.
- [ ] Não há elementos focáveis escondidos (ex: menu fechado mantendo `tabindex="0"`).

## 2. Teclado

- [ ] Todo conteúdo e funcionalidade são operáveis apenas com teclado (`Tab`, `Shift+Tab`, `Enter`, `Space`, `Esc`, setas).
- [ ] Checklists (`DopamineChecklist`, `WinsChecklist`) usam `<button>` ou `<input type="checkbox">` nativos.
- [ ] Acordeões de currículo e FAQ respondem às teclas `Enter`, `Space` e `Esc`.
- [ ] Foco visível é claro (outline de pelo menos 2 px de contraste).
- [ ] Ordem de foco segue a ordem visual da página.

## 3. Leitor de tela

- [ ] Imagens informativas possuem `alt` descritivo; decorativas usam `alt=""`.
- [ ] Botões e links possuem rótulos compreensíveis fora de contexto (ex: "Comprar agora — TDAH Descomplicado").
- [ ] Ícones isolados possuem `aria-label` ou texto visível.
- [ ] Notificações de compra e resultados de quiz usam região `aria-live="polite"`.
- [ ] O timer de foco anuncia início/pausa/fim para o leitor de tela.

## 4. Contraste e legibilidade

- [ ] Contraste entre texto e fundo é ≥ 4,5:1 para corpo e ≥ 3:1 para grandes.
- [ ] Botões primários atendem contraste mínimo de 3:1 (texto sobre fundo colorido).
- [ ] Ícones e elementos gráficos essenciais têm contraste ≥ 3:1.
- [ ] Não há texto sobre imagem sem overlay suficiente.

## 5. Motion e distração (foco para TDAH)

- [ ] A consulta de mídia `prefers-reduced-motion` é respeitada e desativa autoplay e pulsações.
- [ ] Não há autoplay de áudio/vídeo sem controle explícito do usuário.
- [ ] Animações em loop (badges, notificações, pulsações) podem ser pausadas ou aparecem no máximo 3×.
- [ ] Transições de entrada são suaves (≤ 300 ms) e não disparam simultaneamente em massa.
- [ ] Não há efeitos de piscar/flash com frequência 3 Hz ou mais.

## 6. Toque e responsividade

- [ ] Todos os alvos de toque medem pelo menos 44 × 44 px (recomendado 48 × 48 px).
- [ ] Botões e links não ficam colados demais em telas pequenas.
- [ ] A página é totalmente navegável em 320 px de largura sem scroll horizontal.
- [ ] Fontes podem ser ampliadas até 200% sem perda de função ou corte de texto.

## 7. Formulários e interação

- [ ] Campos de e-mail (lead-magnet) têm label visível ou `aria-label`.
- [ ] Estados de erro são anunciados por `aria-live` e associados via `aria-describedby`.
- [ ] Modal de checkout (se mantido) usa `<dialog>` ou `role="dialog"` com `aria-modal="true"`.
- [ ] Foco é preso dentro do modal aberto e retornado ao gatilho ao fechar.

## 8. Conteúdo e linguagem

- [ ] Sentenças são curtas e objetivas (≤ 20 palavras quando possível).
- [ ] Blocos de texto longos são divididos por subtítulos, listas ou espaçamento.
- [ ] Termos técnicos são explicados na primeira ocorrência.
- [ ] Prova social parece genuína; contadores e notificações não induzem urgência falsa.

## 9. Ferramentas recomendadas

- **Automatizado:** Lighthouse, axe-core, WAVE.
- **Navegadores:** Chrome + Firefox com leitores de tela (NVDA/JAWS/VoiceOver).
- **Inspeção:** DevTools → Accessibility tree + Computed contrast.
- **Teste real:** convidar 2-3 usuários com TDAH para tarefas simples (encontrar preço, iniciar quiz, comprar).

---

## Registro de testes

| Data | Versão | Ferramenta | Erros encontrados | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

---

*Checklist baseado em WCAG 2.2, COGA e práticas de design neuroinclusivo. Gerado em 2026-06-29.*
