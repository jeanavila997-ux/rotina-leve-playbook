# Revisão dos Templates vLLM Ascend

**Fonte oficial comparada:** [vLLM Ascend Design Documents](https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/Design_Documents/index.html)  
**Repositório:** https://github.com/vllm-project/vllm-ascend  
**Data da revisão:** 2026-06-26  

---

## Resumo executivo

Os 14 templates extraídos são um bom esqueleto de referência para uso no ecossistema ComfyUI, mas **ainda não estão prontos para publicação como documentação técnica**. A maioria está resumida demais e alguns contêm afirmações imprecisas ou desatualizadas em relação à documentação oficial.

Principais riscos encontrados:

1. **`09_context_parallel.md`**: erro factual no valor padrão de `cp_kv_cache_interleave_size`.
2. **`12_npugraph_ex.md`**: mistura conteúdo do design doc com parâmetros não confirmados; precisa de reescrita.
3. **`07_kv_cache_pool.md`**: inconsistência no nome do connector (`AscendStoreConnector` vs `MooncakeStoreConnector`).
4. **`02_cpu_binding.md`**: omite Ascend 950 e detalhes de `--numa-bind` / memória.
5. **`05_eplb.md` e `06_acl_graph.md`**: faltam arquitetura, DFX, diagnósticos e limitações operacionais.
6. **`13_additional_config_reference.md`**: arquivo sintetizado (não vem dos design docs); precisa de nota de escopo e validação extra.

---

## Revisão arquivo por arquivo

### `01_patch_in_vllm_ascend.md` — ✅ Quase correto

**O que está bom:** princípios, estrutura de diretórios, exemplo de patch e limitações estão alinhados com o design doc.

**O que falta/melhorar:**
- O passo 7 do design doc exige **adicionar Unit Test e E2E Test** para qualquer novo patch. Isso não aparece no template.
- O formato da descrição no design doc inclui: `Related PR (if no, explain why)`. O template omite a frase entre parênteses.
- O `__init__.py` correto é `vllm_ascend/patch/platform/__init__.py` (ou worker), não genérico.

**Ação sugerida:** adicionar o passo de testes e manter o formato literal do design doc.

---

### `02_cpu_binding.md` — ⚠️ Incompleto

**O que está bom:** exemplo A3, divisão de papéis básica e limitações iniciais estão corretos.

**O que falta/melhorar:**
- **Ascend 950** não é mencionado. O design doc dedica uma seção a ele: usa `global_slice`, não faz IRQ binding, requer no mínimo **3 CPUs por NPU**, e reparte `pool[:-2]` para main worker.
- A tabela de estratégia está simplificada demais. A3 **e** Ascend 950 usam `global_slice`; A2 / Atlas 300 usam `topo_affinity`, com fallback para `global_slice` quando topo não está disponível.
- Faltam os passos condicionais: **migração de memória (`migratepages`)** e IRQ binding quando `/proc/irq` é gravável.
- Faltam as fontes de entrada (`/proc/self/status`, `npu-smi info -m`, `npu-smi info -t topo`, `lscpu -e=CPU,NODE`).
- `--numa-bind` é convertido para `enable_cpu_binding`, enquanto `--numa-bind-nodes` e `--numa-bind-cpus` são ignorados.

**Ação sugerida:** reescrever a seção de estratégias incluindo Ascend 950, tabela de mínimos de CPUs e fluxo condicional de host tuning.

---

### `03_prepare_inputs.md` — ⚠️ Incompleto

**O que está bom:** a explicação dos níveis de variáveis e o exemplo de prefill estão presentes.

**O que falta/melhorar:**
- O design doc possui um **Step 2: Chunked prefill** com novos token IDs e uma block table atualizada. O template para no Step 1.
- A notação `T_3_2`, `T_3_3`, etc. do design doc foi simplificada para `T_2_2...T_2_4`, o que perde a semântica de "tokens do request 2 a partir da posição 2".
- Faltam as fórmulas explícitas de `block table indices`, `device block number`, `block offsets` e `slot mapping`.

**Ação sugerida:** adicionar o Step 2 e manter as fórmulas passo a passo do design doc.

---

### `04_disaggregated_prefill.md` — ✅ Quase correto

**O que está bom:** fluxos pull/push, classes de interface, tabela de compatibilidade e limitações estão corretos.

**O que falta/melhorar:**
- O design doc tem uma seção **DFX Analysis** com:
  - validação de parâmetros do KV transfer,
  - detecção de conflito de portas,
  - validação do PD ratio.
- Faltam os links para o guia de deployment do Mooncake.

**Ação sugerida:** adicionar seção DFX e referências aos tutoriais oficiais.

---

### `05_eplb.md` — ❌ Muito resumido

**O que está bom:** a tabela de configuração está presente.

**O que falta/melhorar:**
- Arquitetura completa do módulo (`adaptor`, `core/policy`, `eplb_updator`, etc.).
- Os algoritmos de política: `policy_default_eplb`, `policy_swift_balancer`, `policy_flashlb`, `policy_random`.
- Diferença entre **hierarchical** e **global load balancing**.
- Como adicionar uma nova política e como adicionar um novo modelo MoE (ex: `vllm_adaptor.py`, `eplb_utils.py`, `model_register`).
- Seção **DFX** do design doc: validação de inteiros, caminho de arquivo, consistência do expert map e expert weight.
- Link para o user guide de EPLB.

**Ação sugerida:** expandir para ~3x o tamanho atual, cobrindo arquitetura, políticas e DFX.

---

### `06_acl_graph.md` — ⚠️ Incompleto

**O que está bom:** visão geral, capture sizes, restrições Ascend e mecanismo de update de attention estão corretos.

**O que falta/melhorar:**
- Referências aos docs upstream de CUDA Graphs e PyTorch.
- Seção de **diagnósticos e operações**: como confirmar que graph mode está ativo (`--cudagraph-metrics`, não passar `--disable-log-stats`), debug mode com assert de endereços, etc.
- A informação de que `cudagraph_capture_sizes` e `max_cudagraph_capture_size` são as alavancas principais quando capture falha.
- A ressalva de que `update_aclgraph_sizes()` foi removido em versões recentes.

**Ação sugerida:** adicionar seção de diagnóstico e tuning operacional.

---

### `07_kv_cache_pool.md` — ⚠️ Inconsistência de nome

**O que está bom:** motivação, arquitetura multi-tier e métodos do connector estão bem cobertos.

**O que falta/melhorar:**
- **Nome do connector:** o design doc diz para escolher `MooncakeStoreConnector`. O template usa `AscendStoreConnector` no exemplo de configuração — precisa ser confirmado/ajustado.
- Faltam as limitações do design doc:
  - Apenas DRAM é suportada como storage no momento.
  - Falha de `get` gera log de erro e a request continua, mas a acurácia pode ser afetada.
- Faltam detalhes do DFX (quando não há cache hit, pare; quando put falha, pare).

**Ação sugerida:** corrigir o nome do connector e adicionar DFX + limitações oficiais.

---

### `08_custom_aclnn_op.md` — ✅ Quase correto

**O que está bom:** passos básicos, estrutura de diretórios e meta implementation estão presentes.

**O que falta/melhorar:**
- Poderia mencionar que os ops são built/installed em `vllm_ascend/cann_ops_custom`.
- A tabela de meta functions no template lista funções específicas do código (`get_masked_input_and_mask_meta`, `grouped_matmul_swiglu_quant`, `mla_preprocess`), mas o design doc não as enumera. Seria mais seguro dizer "exemplos de meta functions existentes".

**Ação sugerida:** pequenos ajustes de escopo e precisão.

---

### `09_context_parallel.md` — ❌ Erro factual

**O que está bom:** visão geral de PCP/DCP, comandos de uso e tabela de compatibilidade.

**O que precisa de correção urgente:**
- O template diz: `cp_kv_cache_interleave_size = block_size (default 128)`.  
  **Errado.** O design doc afirma: `cp_kv_cache_interleave_size=1` é o padrão (token interleave). A restrição é `block_size % cp_kv_cache_interleave_size == 0`.
- Faltam as fórmulas de mapeamento de blocos virtuais:
  - `virtual_block_size = block_size * cp_size`
  - `target_rank = local_block_index % cp_size`
- Faltam os detalhes do DCP: all-gather no eixo de heads para GQA, `cp_lse_ag_out_rs`, `reorg_kvcache` para MLA.
- Faltam os detalhes do PCP: particionamento head-tail, `_update_tokens_for_pcp`, abordagens AllGatherQ / AllGatherKV / Ring-Attn para chunked prefill.
- Faltam os arquivos relacionados (`block_table.py`, `model_runner_v1.py`, `pcp_utils.py`, `attention_cp.py`, `mla_cp.py`, `dsa_cp.py`, `sfa_cp.py`).

**Ação sugerida:** corrigir o default e expandir com as fórmulas e arquivos do design doc.

---

### `10_dynamic_chunked_pipeline_parallel.md` — ⚠️ Incompleto

**O que está bom:** problema, modelo quadrático, fases de profiling/runtime e parâmetros estão corretos.

**O que falta/melhorar:**
- **Online calibration**: modelo estendido `f(C, H) = a·C(C+H) + b·(C+H) + c`, acumulação de 5-30 amostras e atualização por least squares.
- Tabela de **key components** (`ChunkSizePredictor`, `ProfilingChunkManager`, `Scheduler`, `EngineCore`, `NPUWorker`, `NPUModelRunner`) e localização dos arquivos.
- Comparação com SGLang (método de profiling, online updates, startup cost).
- Arquitetura/workflow em duas fases (startup e runtime).
- Limitações: incompatível com `VLLM_ASCEND_BALANCE_SCHEDULING`, overhead de dezenas de segundos, sem overhead de memória adicional.

**Ação sugerida:** adicionar calibração online, componentes e comparação.

---

### `11_quantization_adaptation.md` — ✅ Quase correto

**O que está bom:** processo de quantização, algoritmos suportados e passos de adaptação estão corretos.

**O que falta/melhorar:**
- A explicação de **static vs dynamic** e **granularity** no final do design doc é útil e deveria constar.
- O arquivo de mapping é `vllm_ascend/quantization/modelslim_config.py`, não apenas `packed_modules_model_mapping`.
- A tabela de algoritmos poderia incluir a coluna **Description** do design doc.

**Ação sugerida:** adicionar notas sobre static/dynamic/granularity e referência ao arquivo correto.

---

### `12_npugraph_ex.md` — ❌ Precisa ser reescrito

**O que está bom:** introdução diz que é baseado em FX graphs.

**O que está errado/sem base no design doc:**
- "Será habilitado por padrão no futuro" — **não consta** no design doc.
- "Habilitado por padrão em FULL / FULL_DECODE_ONLY mode" — **não consta** no design doc.
- A tabela de configurações (`enable_npugraph_ex`, `enable_static_kernel`, `fuse_norm_quant`, etc.) não vem do design doc analisado. Parece vir de outro guia ou versão; sem fonte no doc, é arriscado manter como template oficial.

**O que falta do design doc:**
- FX graph pass padrão: substituição de operadores não in-place por in-place e reversão do processo funcionalize do Dynamo.
- FX fusion pass e link para a lista oficial.
- **Custom fusion pass** com API `register_replacement(search_fn, replace_fn, example_inputs, trace_fn, extra_check, search_fn_pattern)` e exemplo completo.
- DFX: uso de `TORCH_COMPILE_DEBUG=1` para inspecionar FX graphs.

**Ação sugerida:** reescrever baseado estritamente no design doc; mover a tabela de configurações para um arquivo separado e marcar como "não confirmado pelo design doc".

---

### `13_additional_config_reference.md` — ⚠️ Escopo não declarado

**O que está bom:** tabela de configurações adicionais é útil como referência rápida.

**O que falta/melhorar:**
- Esse arquivo **não é um design doc**; é uma referência sintetizada. Deve ter uma nota clara de escopo e versão, e indicar que os defaults precisam ser validados com o código/user guide atual.
- `enable_npugraph_ex` está listado com default `False`, mas a fonte não foi confirmada nesta revisão.
- A tabela de migração de env vars é boa, mas deveria indicar quais ainda são suportados na versão atual.

**Ação sugerida:** adicionar disclaimer de escopo e data de validação.

---

### `14_comfyui_integration_notes.md` — ✅ Adequado

**O que está bom:** contexto, mapeamento de conceitos e estrutura de arquivos estão razoáveis.

**O que melhorar:**
- Atualizar a lista de documentos extraídos para refletir que há 11 design docs oficiais + 2 arquivos extras (`additional_config_reference` e `comfyui_integration_notes`).
- Adicionar uma nota de que os templates devem ser validados contra a versão do vllm-ascend que será usada no custom node.

---

## Recomendações gerais

1. **Adicionar links oficiais em cada template.** Todo template deve citar a fonte oficial e o arquivo original do repositório.
2. **Data/versão no cabeçalho.** vLLM Ascend evolui rápido; incluir `Baseado em: docs.vllm.ai/projects/ascend/en/latest/...` e data.
3. **Separar "design doc template" de "referência operacional".** O arquivo 13 é o único que foge do escopo; mantê-lo como referência, não template.
4. **Manter terminologia em português consistente.** Alguns termos técnicos podem permanecer em inglês (ex: `slot mapping`, `chunked prefill`) para evitar ambiguidade.
5. **Adicionar uma seção "Checklist antes de usar"** em cada template com pré-requisitos de hardware/ambiente.
6. **Corrigir `09_context_parallel.md` e reescrever `12_npugraph_ex.md` antes de qualquer uso público.**

---

## Próximos passos propostos

- [ ] Corrigir os erros identificados acima.
- [ ] Expandir os templates marcados como incompletos (`02`, `05`, `06`, `09`, `10`, `12`).
- [ ] Gerar uma **versão 2.0** dos templates em uma subpasta `revisados/`.
- [ ] Adicionar um `README.md` com o propósito do projeto e instruções de manutenção.

Se quiser, posso gerar os arquivos corrigidos agora em `C:\Users\jeanc_pmc3uv0\Downloads\tdah-descomplicado\criativos-neon\novos templates\revisados\`.
