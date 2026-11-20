# Curso de Python – projetos aula a aula

Código-fonte das aulas de **Python** (Lógica de Programação, Programação Orientada a Objetos e Django),
organizado **uma pasta por aula**, com `README.md` explicando o conteúdo e o código **modernizado** para o
Python 3.12+.

> Material didático baseado no curso do **Prof. Fabrício Curvello**
> ([playlist no YouTube](https://www.youtube.com/playlist?list=PLIn2kYkmuf41bAWw2Ve_cd4TS2ixm78_c)).
> O código foi reescrito a partir dos conceitos de cada aula. Os slides, no padrão visual SENAI, estão em [`material-slides`](material-slides).

## Slides e listas de exercícios

A pasta [`material-slides`](material-slides) reúne o material de aula no padrão visual SENAI (Firjan), em **`.pptx` e `.pdf`**:

| Pasta | Conteúdo |
| --- | --- |
| [`Python - Modulo 1 - Logica de Programacao`](<material-slides/Python - Modulo 1 - Logica de Programacao>) | Aulas 00 a 09, listas de exercícios (03, 04, 05) e guia PEP 8 |
| [`Python - Modulo 2 - Programacao Orientada a Objetos`](<material-slides/Python - Modulo 2 - Programacao Orientada a Objetos>) | Aulas 10 a 18 |
| [`Python - Modulo 3 - Django`](<material-slides/Python - Modulo 3 - Django>) | Aulas 19 a 29 |

Cada arquivo mantém o número da aula (`Python 05 - ...`), o que facilita relacioná-lo à pasta de código correspondente.
O `.pptx` usa as fontes **Lato Light** e **Nunito Sans**; instale-as para ver o arquivo idêntico ao PDF.

## Como usar

Requer **Python 3.12 ou superior** (`python --version`). Módulos 1 e 2 usam apenas a biblioteca padrão.

```bash
cd modulo-1-logica-de-programacao/aula-05-lacos
python laco_for.py
```

Execute cada arquivo **de dentro da pasta da aula**: alguns importam arquivos vizinhos (`calculos.py`, `util/`).
As listas de exercícios têm um menu: escolha o número do exercício ao iniciar.

## Índice

### Módulo 1 – Lógica de Programação

| Aula | Conteúdo |
| --- | --- |
| [00](modulo-1-logica-de-programacao/aula-00-instalacao) | Instalação do Python e ambiente virtual |
| [01](modulo-1-logica-de-programacao/aula-01-contatos-iniciais) | `print`, variáveis, `help()` |
| [02](modulo-1-logica-de-programacao/aula-02-ide-pycharm) | IDE, primeiro projeto e comentários |
| [03](modulo-1-logica-de-programacao/aula-03-programacao-sequencial) | Entrada/saída, f-strings, operadores · 3 listas de exercícios |
| [04](modulo-1-logica-de-programacao/aula-04-decisao-e-operadores-ternarios) | `if`/`elif`/`else`, ternário, `match` · 2 listas |
| [05](modulo-1-logica-de-programacao/aula-05-lacos) | `while`, `for`, `break`, `continue` · 2 listas + jogo de adivinhação |
| [06](modulo-1-logica-de-programacao/aula-06-funcoes) | Funções, `*args`, `lambda`, `__main__` |
| [07](modulo-1-logica-de-programacao/aula-07-listas-tuplas-dicionarios-conjuntos) | Listas, tuplas, dicionários, conjuntos |
| [08](modulo-1-logica-de-programacao/aula-08-leitura-e-escrita-em-arquivos) | Arquivos com `with` e `pathlib` |
| [09](modulo-1-logica-de-programacao/aula-09-recursos-string) | Fatiamento, escapes, métodos de `str` |

### Módulo 2 – Programação Orientada a Objetos

| Aula | Conteúdo |
| --- | --- |
| [10](modulo-2-poo/aula-10-classes-e-objetos) | Classes e objetos, `@dataclass` |
| [11](modulo-2-poo/aula-11-metodos) | Métodos |
| [12](modulo-2-poo/aula-12-ocultamento-e-encapsulamento) | Ocultamento, encapsulamento, `@property` |
| [13](modulo-2-poo/aula-13-heranca-e-polimorfismo) | Herança, `__str__`, polimorfismo |
| [14](modulo-2-poo/aula-14-instancia-classe-estatico) | Atributos e métodos de instância × classe × estáticos |
| [15](modulo-2-poo/aula-15-classe-abstrata) | Classes e métodos abstratos (`abc`) |
| [16](modulo-2-poo/aula-16-relacoes-entre-classes) | Associação, agregação, composição |
| [17](modulo-2-poo/aula-17-tratamento-de-erros) | Exceções: `try`/`except`, `raise`, exceções próprias |
| [18](modulo-2-poo/aula-18-modulos) | Módulos, pacotes e `pip` |

### Módulo 3 – Django

Projeto único e cumulativo: [`modulo-3-django`](modulo-3-django) (aulas 19 a 29).

## O que mudou em relação ao material original

- **f-strings** como padrão; `.format()` e `%` aparecem só para comparação (aula 03).
- **PEP 8**: `snake_case`, sem parênteses desnecessários em `if`/`while`, `if __name__ == "__main__":` em tudo.
- **Type hints** e docstrings nas funções e classes.
- **`with open(..., encoding="utf-8")`** e `pathlib` no lugar de `open()`/`close()` manuais.
- **`@property`**, **`@dataclass`**, **`match`/`case`**, `for … else`, desempacotamento e compreensões de lista.
- Entrada de dados validada sem recursão (`util/teclado.py`).
- Django: segredos por variável de ambiente, namespaces de URL, `get_object_or_404`, testes automatizados.
- Bugs dos slides corrigidos (cada README de aula lista o que foi alterado).

## Qualidade

```bash
python -m pip install ruff
ruff check .
```
