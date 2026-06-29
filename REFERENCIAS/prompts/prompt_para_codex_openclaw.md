# Prompt para usar Open Design com Codex / OpenClaw / Kimi

Você é um agente de código conectado ao Open Design.

Use o sistema de design abaixo como contrato visual obrigatório:

- Sistema escolhido: `Ollama`, `OpenAI`, `Neon` ou `Shadcn`
- Arquivo-base: `DESIGN.md`
- Saída desejada: HTML funcional, responsivo, com CSS limpo e pronto para copiar para um app real.

## Tarefa

Crie uma interface web para o seguinte projeto:

```txt
[DESCREVA AQUI O APP OU TELA]
```

## Regras

1. Respeite paleta, tipografia, espaçamento, bordas e componentes do `DESIGN.md`.
2. Gere uma única página HTML com CSS embutido.
3. A interface deve parecer produto real, não wireframe.
4. Inclua estados visuais: hover, foco, botão primário, secundário e cards.
5. Use nomes de classes organizados.
6. Mantenha o código pronto para virar React/Next.js depois.

## Saída esperada

- `index.html`
- resumo das decisões visuais
- sugestões de próximos componentes
