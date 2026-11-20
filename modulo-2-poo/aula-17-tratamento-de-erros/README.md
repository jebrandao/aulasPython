# Aula 17 – POO: tratamento de erros (exceções)

| Arquivo | Assunto |
| --- | --- |
| [`tratamento1_sem_excecoes.py`](tratamento1_sem_excecoes.py) | O erro sem tratamento (o programa **deve** falhar com certas entradas) |
| [`tratamento2_com_excecoes.py`](tratamento2_com_excecoes.py) | `try` / `except` / `else` / `finally` |
| [`tratamento3_lancando_excecoes.py`](tratamento3_lancando_excecoes.py) | `raise` para repassar uma exceção |
| [`tratamento4_lancando_excecoes.py`](tratamento4_lancando_excecoes.py) | `raise ValueError(...)` com validação prévia |
| [`tratamento5_criando_excecoes.py`](tratamento5_criando_excecoes.py) | Exceção própria (herda de `Exception`) |

## Estrutura

```python
try:
    ...  # código que pode falhar
except ValueError as erro:
    ...  # trata um tipo específico
else:
    ...  # só roda se NÃO houve erro
finally:
    ...  # roda SEMPRE (limpeza)
```

## O que foi modernizado

- Nome do arquivo 2 corrigido (`excessoes` → `excecoes`).
- Captura de **exceções específicas**, nunca `except:` puro (ele esconde bugs e até `Ctrl+C`).
- Atenção: `nomes[-1]` é um índice **válido** em Python (o último item), então só números fora de
  `-5..4` geram `IndexError` na lista de 5 nomes.
- `raise ... from erro` preserva a causa original ao converter uma exceção.
- Exceção própria com mensagem padrão e atributo extra.
