# Aula 06 – Funções

Funções permitem **modularizar** e **reaproveitar** código. Definem-se com `def`.

| Arquivo | Assunto |
| --- | --- |
| [`exemplo_funcao1.py`](exemplo_funcao1.py) | Função sem parâmetros |
| [`exemplo_funcao2.py`](exemplo_funcao2.py) | Parâmetros e argumentos |
| [`exemplo_funcao3.py`](exemplo_funcao3.py) | Retorno de valor (`return`) |
| [`calculos.py`](calculos.py) + [`exemplo_calculos.py`](exemplo_calculos.py) | Funções em outro arquivo (`import`) e `if __name__ == "__main__"` |
| [`exemplo_funcao_multiplos_parametros.py`](exemplo_funcao_multiplos_parametros.py) | `*args` |
| [`exemplo_funcao_lambda.py`](exemplo_funcao_lambda.py) | Funções `lambda` |

## `__name__ == "__main__"`

Ao importar um arquivo, **tudo o que está fora de funções é executado**. Para evitar isso, coloque o código de
execução dentro de `if __name__ == "__main__":`. Todos os arquivos deste repositório seguem essa convenção.

## O que foi modernizado

- Type hints (`n1: float`) e docstrings nas funções.
- Funções que **calculam** retornam o valor; funções que **exibem** ficam separadas (`print` fora do cálculo).
- `sum()` no lugar do laço manual de soma, e comentários sobre quando usar `lambda` (e quando preferir `def`).
