# Aula 16 – POO: relações entre classes

| Relação | Ideia | Ciclo de vida | Exemplo |
| --- | --- | --- | --- |
| **Associação** | Um objeto *usa* outro | Independentes | `Pessoa` pratica atividade na `Academia` |
| **Agregação** | O todo *possui* partes que existem por conta própria | Independentes | `CarrinhoDeCompras` contém `Produto`s |
| **Composição** | O todo *cria* as partes e elas só fazem sentido dentro dele | A parte morre com o todo | `Usuario` cria seus `Telefone`s |

| Arquivo | Assunto |
| --- | --- |
| [`relacao1_associacao.py`](relacao1_associacao.py) | Associação |
| [`relacao2_agregacao.py`](relacao2_agregacao.py) | Agregação |
| [`relacao3_composicao.py`](relacao3_composicao.py) | Composição e o método `__del__` |

## Como identificar no código

- **Associação / agregação**: o objeto "parte" é **criado fora** e **recebido** (por atributo ou parâmetro).
- **Composição**: o objeto "parte" é **criado dentro** da classe principal (`Telefone(...)` dentro de
  `Usuario.cadastrar_telefone`).

## O que foi modernizado

- Type hints, incluindo referência à própria classe com `from __future__ import annotations`.
- `__del__` fica apenas como demonstração: em Python ele **não é a forma recomendada** de liberar recursos
  (o momento da execução depende do coletor de lixo; no CPython costuma ser imediato, em outras implementações não).
  Para recursos reais use `with` (gerenciadores de contexto), como na aula 08.
- Valores monetários formatados com f-string.
