# Análise dos Criativos — TDAH Descomplicado

## O que é essa pasta

`C:\Users\jeanc_pmc3uv0\Downloads\tdah-descomplicado\criativos-neon` é um **kit de criativos de marketing** para o lançamento do e-book *TDAH Descomplicado*. Ela contém:

- **5 anúncios Meta Ads** em HTML (1080×1350)
- **1 anúncio estático** com 2 variantes
- **Landing page de vendas** responsiva
- **Carrossel Instagram** e **post Instagram** editáveis em HTML
- **Stories/Reels** com enquete/contador
- **Sequência de 5 e-mails** de nutrição
- **3 roteiros de vídeo** para Reels/TikTok/Shorts
- **Perfil de cliente** e **capa de e-book**

O design system adotado é o **Soft Light (Clean Minimalism)**: paleta suave com índigo `#4F46E5`, azul-celeste `#0EA5E9`, rosa `#F43F5E` e fundo `#FAFBFD`. A proposta é reduzir a carga cognitiva — coerente com o público TDAH.

---

## Pontos Fortes (manter)

1. **Identidade visual coesa** — `:root` com tokens de cor replicados em quase todos os HTMLs.
2. **Copy empática** — linguagem que externaliza a culpa do leitor (“não é você, é seu sistema”).
3. **Estrutura de funil completa** — anúncios → landing → e-mails → scripts de vídeo.
4. **CTAs claros** — “Garantir Meu Kit por R$ 47” e “Fazer Teste Rápido” são diretos.
5. **Garantia e formas de pagamento** visíveis na landing page.
6. **Disclaimer médico** no footer, importante para não parecer tratamento.

---

## Sugestões de Melhoria

### 1. Corrigir inconsistência de nome e design

**Problema:** a pasta se chama `criativos-neon`, mas o design system é **Soft Light**, com cores pastel e fundo claro. Não há “neon” de fato. Isso pode confundir na hora de organizar entregáveis.

**Sugestão:** renomear a pasta/conceito para `criativos-soft-light` ou `criativos-tdah-descomplicado` para refletir o design system real.

---

### 2. Padronizar a paleta nos scripts de vídeo

**Problema:** em `scripts-video.md`, as notas de produção falam em fundo escuro `#0A0A0F` com cores neon `#BBF351` e `#00BCFF`. Isso contradiz o design system Soft Light e os demais criativos.

**Sugestão:** atualizar as notas de produção para usar o Soft Light também nos vídeos, ou criar uma **variante escura** aprovada e documentada no `README.md` para evitar que cada editor use cores diferentes.

---

### 3. Adicionar identidade da marca nos anúncios

**Problema:** os 5 anúncios não mostram logo, nome do produto ou URL. Quando o criativo roda sozinho no feed, o usuário não sabe de quem é.

**Sugestão:**
- Inserir **logo + nome** “TDAH Descomplicado” no topo ou rodapé.
- Incluir a **URL** `tdahdescomplicado.com` ou o **@perfil** do Instagram.
- Adicionar um **selo de garantia de 7 dias** nos anúncios 2, 3, 4 e 5.

---

### 4. Tornar a prova social mais crível

**Problema:** os anúncios repetem “4.9 · 12.847 pessoas já transformaram sua rotina” e “12.847 avaliações”. Esse número genérico pode parecer inventado.

**Sugestão:**
- Substituir por número real de vendas/alunos quando houver.
- Ou usar microprovas sociais mais específicas: “+3.200 pessoas com TDAH diagnosticado já usaram”.
- No `anuncio-4-depoimento-real.html`, a “pessoa” é apenas um emoji 👤 em silhueta genérica. Isso enfraquece o depoimento.

**Ação:** trocar o avatar genérico por uma foto real da Marina (com autorização) ou remover o depoimento até ter imagem real.

---

### 5. Corrigir o CTA “Fazer Teste de Sobrecarga”

**Problema:** na landing page, o botão secundário do hero leva para `#problema`, mas a seção correspondente não tem nenhum teste/quiz. O usuário pode se sentir enganado.

**Sugestão:**
- Criar uma **seção de quiz/teste rápido** na landing page (3 perguntas, sem cadastro) e apontar o botão para ela.
- Ou renomear o botão para “Ver como funciona” e manter o scroll para `#problema`.

---

### 6. Capturar e-mails antes do checkout

**Problema:** o funil de e-mails (`emails-lancamento.md`) é bem estruturado, mas a landing page não tem campo de captura de e-mail. Quem não comprar na primeira visita é perdido.

**Sugestão:** adicionar um **lead magnet** na landing page:
- “Baixe o Guia Rápido: 3 Técnicas de Atrito Zero” em troca do e-mail.
- Ou um **mini-quiz** com resultado por e-mail.
- Isso alimenta a sequência de 5 e-mails já existente.

---

### 7. Criar variações de formato para os anúncios

**Problema:** todos os anúncios estáticos estão em 1080×1350 (feed). Não há versões:
- 1080×1080 (quadrada)
- 1080×1920 (stories/reels)
- 1200×628 (feed do Facebook)

**Sugestão:** gerar variações dos 5 anúncios nos 3 formatos principais para Meta Ads. Isso melhora o desempenho de campanha.

---

### 8. Revisar copy com termos misturados

**Problema:** no `anuncio-5-desafio-7s.html`, aparece a frase “É como seu cérebro está **wired**”. O restante do material é 100% em português.

**Sugestão:** substituir por “É assim que seu cérebro está conectado” ou “É a forma como seu cérebro funciona”.

---

### 9. Corrigir referências quebradas na documentação

**Problema:**
- `README.md` cita `landing-page-neon.html`, mas o arquivo real é `landing-page-soft-light.html`.
- `AGENTS.md` cita o mesmo `landing-page-neon.html`.

**Sugestão:** atualizar ambos os arquivos para o nome correto.

---

### 10. Organizar a pasta “novos templates”

**Problema:** a pasta `novos templates/` contém apenas `revisao.md`, que parece ser uma revisão técnica sobre vLLM/Ascend — totalmente fora do contexto de criativos TDAH.

**Sugestão:**
- Mover `revisao.md` para fora deste projeto, se pertence a outro trabalho.
- Ou renomear a pasta para `rascunhos/` ou `arquivados/` e deixar claro seu propósito.

---

### 11. Melhorar a exportação dos editores HTML

**Problema:** `carrossel-instagram.html` e `post-instagram-soft-light.html` são editores com campos `contenteditable`, mas o botão “Salvar como PDF” é um stub simples. A instrução do README é “Imprimir → Salvar como PDF”, que pode cortar elementos ou gerar qualidade irregular.

**Sugestão:**
- Implementar **html2canvas + jsPDF** ou **Print.js** para gerar PNG/PDF de alta resolução automaticamente.
- Adicionar botões: **Exportar PNG 1080px**, **Exportar PDF**, **Resetar padrão**.

---

### 12. Criar um CSS compartilhado

**Problema:** cada `.html` repete centenas de linhas de CSS (tokens, fontes, reset, utilitários). Manutenção futura é difícil.

**Sugestão:**
- Extrair um arquivo `assets/soft-light.css` com o design system base.
- Importar via `<link rel="stylesheet" href="assets/soft-light.css">`.
- Manter apenas variações específicas dentro de cada arquivo.

---

### 13. Incluir metadados e previews

**Problema:** não há thumbnails ou `.png` de referência dos anúncios, exceto a capa da mulher e uma imagem do Gemini.

**Sugestão:**
- Gerar uma pasta `previews/` com screenshots de cada criativo.
- Isso facilita revisão visual sem abrir cada HTML no navegador.

---

### 14. Testar o checkout em todos os CTA

**Problema:** vários anúncios têm CTA apenas visual (botão fictício) e não redirecionam. Apenas a landing page abre o link da Cakto.

**Sugestão:**
- Adicionar `onclick="window.open('https://pay.cakto.com.br/9u9w6q4_940459', '_blank')"` nos botões dos anúncios que devem converter direto.
- Ou incluir um **QR code** na arte para quem está no feed mobile.

---

### 15. Verificar acessibilidade e legibilidade

**Problema:** alguns textos usam cinza claro (`rgba(30,41,59,0.5)`) sobre fundo `#FAFBFD`. A razão de contraste pode ficar abaixo de 4.5:1 em telas de baixa qualidade.

**Sugestão:**
- Usar `#475569` ou mais escuro para textos secundários.
- Testar contraste com ferramenta como WebAIM Contrast Checker.

---

## Resumo das prioridades

| Prioridade | Ação | Impacto |
|------------|------|---------|
| Alta | Corrigir CTA “Teste de Sobrecarga” ou criar o quiz | Conversão / confiança |
| Alta | Adicionar captura de e-mail na landing page | Nutrição / funil |
| Alta | Padronizar nome da pasta/design system | Organização |
| Média | Inserir logo/URL nos anúncios | Reconhecimento de marca |
| Média | Melhorar prova social (fotos/números reais) | Credibilidade |
| Média | Gerar variações 1080×1080 e 1080×1920 | Alcance de campanha |
| Média | Corrigir referências no README/AGENTS | Documentação |
| Baixa | Extrair CSS compartilhado | Manutenção |
| Baixa | Implementar exportação automática dos editores | Produtividade |

---

## Nota final

O material já está **acima da média** para um kit de lançamento solo. As melhorias acima são ajustes de ponta: maior credibilidade, melhor integração entre anúncios e landing page, e padronização operacional. Nenhuma delas exige refazer o design do zero.
