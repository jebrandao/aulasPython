# Aula 04 – Programação com decisão e operadores ternários

| Arquivo | Assunto |
| --- | --- |
| [`desvio_condicional_simples.py`](desvio_condicional_simples.py) | `if` |
| [`desvio_condicional_composto.py`](desvio_condicional_composto.py) | `if` / `else` |
| [`desvio_condicional_encadeado.py`](desvio_condicional_encadeado.py) | `if` dentro de `else` |
| [`desvio_condicional_encadeado_elif.py`](desvio_condicional_encadeado_elif.py) | `elif` (a última opção é sempre `else`) |
| [`operadores_ternarios.py`](operadores_ternarios.py) | As duas formas de operador ternário |
| [`match_case.py`](match_case.py) | **Extra moderno:** `match`/`case` (Python 3.10+) |

## Exercícios

- [`exercicios/lista_1.py`](exercicios/lista_1.py)
- [`exercicios/lista_2.py`](exercicios/lista_2.py)

## O que foi modernizado

- Sem parênteses desnecessários em `if (condicao):` (PEP 8).
- Comparação encadeada: `100 <= num <= 200` em vez de `num >= 100 and num <= 200`.
- O ternário com tupla indexada `("a", "b")[condicao]` é mostrado só como curiosidade: ele avalia as duas
  opções antes de escolher. A forma idiomática é `valor_se_verdadeiro if condicao else valor_se_falso`.
- `match`/`case` para escolhas entre vários valores (dia da semana, opções de menu).
