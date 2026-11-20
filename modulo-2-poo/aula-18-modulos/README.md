# Aula 18 – Módulos e pacotes

- **Módulo**: um arquivo `.py` cujas definições podem ser importadas.
- **Pacote**: uma pasta com módulos (aqui, `util/`).
- **PIP**: instala bibliotecas de terceiros do [PyPI](https://pypi.org).

## Estrutura

```text
aula-18-modulos/
├── calculadora.py            # módulo próprio
├── calculos1.py              # import calculadora
├── calculos2.py              # from calculadora import somar, ...
├── calculos3.py              # from calculadora import *   (evitar)
├── modulos_padroes1.py       # import random, math
├── modulos_padroes2.py       # from ... import ... as ...
├── modulos_padroes3.py       # from ... import *            (evitar)
├── util/                     # pacote
│   ├── __init__.py
│   └── teclado.py            # ler_str, ler_int, ler_float
└── questionario1.py … 4.py   # as 4 formas de importar do pacote
```

> Execute os arquivos **de dentro desta pasta** (`python questionario1.py`) para que o Python encontre `util/`.

## Formas de importar

| Forma | Uso | Comentário |
| --- | --- | --- |
| `import modulo` | `modulo.funcao()` | Claro de onde vem cada nome |
| `import modulo as m` | `m.funcao()` | Apelido para nomes longos |
| `from modulo import funcao` | `funcao()` | Importa só o necessário |
| `from modulo import *` | `funcao()` | **Evite**: polui o espaço de nomes e esconde a origem dos nomes |

## Módulos de terceiros (PIP) em ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate           # Windows   (macOS/Linux: source .venv/bin/activate)
python -m pip install --upgrade pip
python -m pip install requests   # instalar
python -m pip list               # listar
python -m pip uninstall requests # remover
python -m pip freeze > requirements.txt   # registrar dependências
```

Usar `python -m pip` garante que o `pip` pertence ao mesmo Python que executa seu código.

## Correções e modernizações em relação aos slides

- `ler_int` do slide usava `try/except/finally` com `return` dentro do `finally` e **recursão**, o que engole
  qualquer exceção (inclusive `Ctrl+C`) e pode estourar a pilha. Agora é um laço `while True` capturando só
  `ValueError`.
- `ler_float` (o desafio da aula) também aceita o formato brasileiro (`1.234,56` ou `1234,56`) além de `1234.56`.
- `from math import pow` **esconde** a função embutida `pow()`; o exemplo usa apelido para evitar a confusão.
- `util/__init__.py` explícito (pacotes sem ele também funcionam, mas o arquivo documenta a intenção).
