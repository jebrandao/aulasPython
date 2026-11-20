# Aula 07 – Listas, tuplas, dicionários e conjuntos

| Estrutura | Declaração | Característica |
| --- | --- | --- |
| Lista (`list`) | `[ ]` | Ordenada, **mutável**, indexada por posição |
| Tupla (`tuple`) | `( )` | Ordenada, **imutável** |
| Dicionário (`dict`) | `{chave: valor}` | Indexado por **chave** |
| Conjunto (`set`) | `{ }` | Sem ordem, **sem repetição** (`set()` cria um conjunto vazio; `{}` cria um dict) |

| Arquivo | Assunto |
| --- | --- |
| [`exemplo_list.py`](exemplo_list.py) | Métodos de lista (`append`, `insert`, `remove`, `sort`, `reverse`…) |
| [`for_list.py`](for_list.py) | Percorrer listas, `enumerate` e busca de todas as posições |
| [`exemplo_tupla.py`](exemplo_tupla.py) | Tuplas e fatiamento |
| [`exemplo_dicionario.py`](exemplo_dicionario.py) | Dicionários (`get`, `update`, `pop`, `items`…) |
| [`exemplo_conjunto.py`](exemplo_conjunto.py) | Conjuntos, união e interseção |
| [`exemplo_funcao_media.py`](exemplo_funcao_media.py) | Função que trabalha com lista de dicionários |

## O que foi modernizado

- `pop()` (remove e devolve) ao lado de `del`; `sorted()` (cria nova lista) ao lado de `sort()` (altera a original).
- Compreensão de lista e `enumerate` na busca de posições (`for_list.py`).
- Operadores de conjunto (`|`, `&`, `-`) além de `union`/`intersection`.
- Operador `|` para mesclar dicionários (Python 3.9+) e `dict.get()` quando a chave pode não existir.
- `sum()` na média e conferência com `statistics.mean`.
- O slide adiciona "Maria" duas vezes à lista `donos`; aqui o novo dono é "Ana" para o resultado ficar mais claro.
