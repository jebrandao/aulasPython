# Aula 13 – POO: herança e polimorfismo

- **Herança**: a subclasse (`Aluno`, `Professor`) recebe atributos e métodos da superclasse (`Pessoa`) e
  acrescenta só o que é específico. O construtor da filha repassa os dados da mãe com `super().__init__(...)`.
- **`object` e `__str__`**: toda classe herda de `object`. Sobrescrever `__str__` define o que `print(objeto)` exibe
  (equivalente ao `toString()` de outras linguagens).
- **Polimorfismo**: a subclasse **sobrescreve** um método herdado para ter comportamento próprio
  (`ContaEspecial.calcular_saldo()` soma o limite ao saldo).

| Arquivo | Assunto |
| --- | --- |
| [`heranca.py`](heranca.py) | `Pessoa`, `Aluno`, `Professor` com `@property` |
| [`metodo_str.py`](metodo_str.py) | `__str__` em uma classe simples |
| [`heranca_metodo_str.py`](heranca_metodo_str.py) | `__str__` com herança, reaproveitando `super().__str__()` |
| [`polimorfismo.py`](polimorfismo.py) | `ContaCorrente` × `ContaEspecial` e `calcular_saldo()` |
| [`heranca_dataclass.py`](heranca_dataclass.py) | **Extra moderno:** herança com `@dataclass` |

## Correções em relação aos slides

- Em `ContaCorrente`, o setter do saldo estava declarado como `@titular.setter`.
- `calcularSaldo` virou `calcular_saldo` (`snake_case`).
- A máscara da conta (`123456-7`) usa f-string em vez de `.format()`.

## O que foi modernizado

- Type hints e `super()` sem argumentos.
- `@dataclass` com herança: a subclasse acrescenta campos e o `__init__`/`__repr__` são gerados sozinhos.
- Em `polimorfismo.py`, uma lista de contas diferentes é somada chamando o mesmo método em todas.
