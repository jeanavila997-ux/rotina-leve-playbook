# Comandos para extrair os arquivos originais

## 1. Clonar o repositório

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design
```

## 2. Entrar na pasta dos sistemas de design

```bash
cd plugins/_official/design-systems
```

## 3. Listar todos os sistemas disponíveis

```bash
ls
```

## 4. Copiar apenas os sistemas úteis para nossos projetos

```bash
mkdir -p ~/open-design-sistemas-extraidos
cp -r openai ollama neon shadcn vercel supabase linear notion stripe github ~/open-design-sistemas-extraidos/
```

## 5. Ver os arquivos de um sistema

```bash
ls openai
cat openai/DESIGN.md
cat openai/open-design.json
```

## 6. Instalar o Open Design no agente de código

Exemplo com Codex:

```bash
curl -fsSL https://open-design.ai/install.sh | sh -s codex
```

Exemplo com Kimi:

```bash
curl -fsSL https://open-design.ai/install.sh | sh -s kimi
```

Exemplo com OpenClaw:

```bash
curl -fsSL https://open-design.ai/install.sh | sh -s openclaw
```

## 7. Rodar local com Docker

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
```

Depois abra:

```txt
http://localhost:7456
```
