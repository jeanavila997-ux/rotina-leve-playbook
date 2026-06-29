# Próximos Passos — Rotina Leve Playbook

Este arquivo lista o que ainda falta para deixar o produto pronto para venda e entrega.

## ✅ O que já está pronto

- [x] Ebook completo em `content/playbook.md` (31 capítulos, ~20.150 palavras)
- [x] Capítulos separados em `content/playbook/`
- [x] Script de compilação `scripts/compile.py`
- [x] Script de exportação para PDF `scripts/export_pdf.py`
- [x] PDF gerado: `content/rotina-leve-playbook.pdf` (67 páginas, ~609 KB)
- [x] Landing page `landing/index.html` com estrutura de vendas
- [x] Repositório salvo no GitHub

## ⏳ O que ainda falta

### 1. Dados reais na landing page
A landing ainda usa placeholders. Precisa substituir por:

- **Link de checkout da Cakto**: atualmente `https://pay.cakto.com.br/SEU-LINK-AQUI`
- **E-mail de suporte**: atualmente `mailto:suporte@rotinaleve.com`

Arquivo: `landing/index.html`

### 2. Assets visuais para o hero
A landing ainda não tem capa real. Criar:

- Capa 3:4 do ebook em alta resolução (imagem, não CSS)
- Mockups de dispositivos (celular/tablet/notebook mostrando o PDF)
- Favicon e ícone para redes sociais

Sugestão de destino: `landing/assets/`

### 3. Página de obrigado (pós-compra)
Criar `landing/obrigado.html` com:

- Confirmação da compra
- Botão de download do PDF
- Link para grupo/comunidade (WhatsApp/Telegram/Discord) se houver
- Instruções simples de acesso ao material

### 4. Fluxo de entrega pós-compra
Configurar na Cakto:

- Link de download automático ou página de obrigado como URL de redirecionamento
- Envio do PDF por e-mail após a compra
- Testar compra fictícia para garantir entrega

### 5. Publicar a landing page
Escolher onde hospedar:

- **GitHub Pages** (grátis, rápido, ideal para começar)
- **Netlify** (grátis, com DNS próprio fácil)
- **Vercel** (grátis, bom desempenho)

Depois configurar:

- Domínio personalizado (ex: `rotinaleve.com.br`)
- HTTPS automático
- Meta tags de compartilhamento (Open Graph / Twitter Cards)

### 6. SEO e compartilhamento
Atualizar `landing/index.html` com:

- `<title>` descritivo
- Meta description
- Open Graph: `og:title`, `og:description`, `og:image`, `og:url`
- Twitter Card equivalentes
- Favicon

### 7. Testes finais
Antes de divulgar:

- [ ] Abrir a landing no celular e no desktop
- [ ] Testar botão de compra com link real da Cakto
- [ ] Testar download do PDF
- [ ] Testar envio de e-mail de suporte
- [ ] Verificar velocidade de carregamento

## 📋 Resumo das prioridades

| Prioridade | Tarefa | Responsável |
|------------|--------|-------------|
| Alta | Substituir placeholders na landing | Dono do produto |
| Alta | Configurar checkout e entrega na Cakto | Dono do produto |
| Média | Criar capa e mockups | Designer/AI |
| Média | Criar página de obrigado | Desenvolvedor |
| Média | Publicar landing | Desenvolvedor |
| Baixa | SEO, favicon e testes finais | Desenvolvedor |

## 💡 Notas

- Todo o conteúdo do produto digital está finalizado.
- O que falta agora é principalmente configuração comercial e visual.
- O repositório já está pronto para receber essas atualizações.
