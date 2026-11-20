# Aula 08 – Leitura e escrita em arquivos

`open(arquivo, modo)` abre um arquivo. Modos principais:

| Modo | Significado |
| --- | --- |
| `"w"` | Escrita: **cria ou sobrescreve** |
| `"a"` | Escrita ao final (*append*), preservando o conteúdo |
| `"r"` | Leitura (o slide original cita `c` por engano) |

| Arquivo | Assunto |
| --- | --- |
| [`escrita.py`](escrita.py) | `write()` com `w` e `a`; o `\n` quebra linha |
| [`leitura_completa.py`](leitura_completa.py) | `read()` e o "ponteiro de fluxo" |
| [`leitura_linha_a_linha.py`](leitura_linha_a_linha.py) | `for linha in arquivo`, `readline()`, `strip()` |
| [`leitura_para_lista.py`](leitura_para_lista.py) | Carregar as linhas em uma lista |
| [`palavras.txt`](palavras.txt) | Arquivo de exemplo usado pelas leituras |

Ordem sugerida: `escrita.py` → `leitura_completa.py` → `leitura_linha_a_linha.py` → `leitura_para_lista.py`.

## O que foi modernizado

- **`with open(...)`**: fecha o arquivo automaticamente, mesmo se ocorrer erro. Dispensa `close()`.
- **`encoding="utf-8"`** explícito: sem ele o Windows pode usar outra codificação e quebrar acentos.
- **`pathlib.Path(__file__).parent`**: o arquivo é sempre encontrado ao lado do script, não importa de qual
  pasta o programa foi executado.
- `Path.read_text()` / `Path.write_text()` / `splitlines()` como atalhos para casos simples.
