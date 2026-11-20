# Aula 14 – POO: instância × classe × estático

## Atributos

| Escopo | Onde é declarado | Valor |
| --- | --- | --- |
| **Instância** | `self.x = ...` dentro do `__init__` | Individual de cada objeto |
| **Classe** | direto no corpo da classe (`cor = "Amarelo"`) | Compartilhado por todos |

## Métodos

| Tipo | Decorador | Primeiro parâmetro | Acessa |
| --- | --- | --- | --- |
| Instância | (nenhum) | `self` | dados do objeto e da classe |
| Classe | `@classmethod` | `cls` | dados da classe |
| Estático | `@staticmethod` | (nenhum) | nada da classe/objeto; é uma função "morando" na classe |

| Arquivo | Assunto |
| --- | --- |
| [`instancia_x_classe_x_estatico.py`](instancia_x_classe_x_estatico.py) | Exemplo da cooperativa *Táxi Rio* |

## Correções em relação aos slides

- `@ano.setter` estava com `def fabricante(...)`.
- Os métodos foram renomeados para `snake_case` consistente e o código final é apresentado completo (os
  slides o constroem em várias etapas).

## Cuidado

Alterar o atributo de classe pela **classe** (`TaxiRio.cor = "Azul"`) afeta todos os objetos. Atribuir pela
**instância** (`taxi1.cor = "Azul"`) cria um atributo de instância que apenas "esconde" o da classe naquele objeto.
O exemplo demonstra as duas situações.
