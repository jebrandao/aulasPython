# Aula 10 – POO: classes e objetos

- **Classe**: molde com **atributos** (características) e **métodos** (comportamentos).
- **Objeto**: instância de uma classe, com seus próprios valores.
- **Abstração**: modelar só o que importa para o sistema (um `Carro` no estacionamento guarda placa e modelo;
  numa autopeças precisaria listar as peças).

## Nomenclatura (PEP 8)

| O quê | Padrão | Exemplo |
| --- | --- | --- |
| Classes | `PascalCase` | `Carro`, `VeiculoTerrestre` |
| Variáveis, atributos, funções, arquivos | `snake_case` | `data_de_nascimento` |

## Arquivos

| Arquivo | Assunto |
| --- | --- |
| [`classes_objetos.py`](classes_objetos.py) | Classe `Carro`, `__init__`, dois objetos |
| [`classes_objetos_dataclass.py`](classes_objetos_dataclass.py) | **Extra moderno:** a mesma classe com `@dataclass` |

## O que foi modernizado

- Type hints nos atributos e parâmetros.
- `@dataclass` gera `__init__`, `__repr__` e `__eq__` automaticamente (Python 3.7+), evitando código repetitivo.
