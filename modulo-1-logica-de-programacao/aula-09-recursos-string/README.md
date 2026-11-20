# Aula 09 – Alguns recursos de String

| Arquivo | Assunto |
| --- | --- |
| [`operacoes_strings.py`](operacoes_strings.py) | Indexação, fatiamento (`[ini:fim:passo]`), `in`, percorrer caracteres |
| [`sequencias_escape.py`](sequencias_escape.py) | `\n`, `\t`, `\"`, `\\`… e *raw strings* |
| [`metodos_strings.py`](metodos_strings.py) | **Extra:** métodos úteis (`upper`, `split`, `join`, `replace`…) |

## Sequências de escape

| Sequência | Efeito |
| --- | --- |
| `\\` | Barra invertida |
| `\'` / `\"` | Aspas simples / duplas |
| `\n` | Nova linha |
| `\t` | Tabulação horizontal |
| `\r` | Retorno de carro |
| `\b` | Backspace |
| `\a` | Alerta sonoro |
| `\f` / `\v` | Avanço de página / tabulação vertical |

## Observação

Strings são **imutáveis**: `texto[0] = "r"` gera `TypeError`. Métodos como `upper()` devolvem uma
nova string.
