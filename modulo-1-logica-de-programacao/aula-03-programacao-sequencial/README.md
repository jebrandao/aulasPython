# Aula 03 – Programação sequencial

Todo programa tem três etapas: **entrada de dados → processamento → saída de dados**.

## Exemplos da aula

| Arquivo | Assunto |
| --- | --- |
| [`entrada_de_dados.py`](entrada_de_dados.py) | `input()` sempre devolve `str`; conversão com `int()`/`float()` |
| [`variaveis.py`](variaveis.py) | Declaração, `type()` e conversões |
| [`interpolacao_string.py`](interpolacao_string.py) | `print` com vírgulas × `.format()` × **f-string** × `%` |
| [`interpolacao_string_float.py`](interpolacao_string_float.py) | Formatação de `float` (casas decimais, milhar, %, R$) |
| [`interpolacao_string_int.py`](interpolacao_string_int.py) | Formatação de `int` (largura e zeros à esquerda) |
| [`interpolacao_string_cpf.py`](interpolacao_string_cpf.py) | `zfill` e fatiamento para máscara de CPF |
| [`recursos.py`](recursos.py) | Módulo `math` (`sqrt`, `pow`, `pi`) |
| [`operadores.py`](operadores.py) | Operadores aritméticos, relacionais e lógicos |

## Exercícios

Resolução sugerida (uma função por questão, escolhida por um menu):

- [`exercicios/lista_1.py`](exercicios/lista_1.py)
- [`exercicios/lista_2.py`](exercicios/lista_2.py)
- [`exercicios/lista_3.py`](exercicios/lista_3.py)

```bash
python exercicios/lista_1.py
```

## O que foi modernizado

- **f-strings** são a forma recomendada. `.format()` e `%` ficam apenas para comparação, pois aparecem em código legado.
- Formatação de números no padrão brasileiro com `str.translate` em vez de várias chamadas encadeadas a `replace`.
- `math.pow` devolve sempre `float`; para inteiros use o operador `**`.
