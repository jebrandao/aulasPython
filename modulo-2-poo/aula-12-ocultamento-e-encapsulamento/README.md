# Aula 12 – POO: ocultamento e encapsulamento

- **Ocultamento**: restringir o acesso direto aos atributos. Em Python é uma **convenção**:
  - `_atributo` → "uso interno", não acesse de fora (nada impede, mas é falta de educação);
  - `__atributo` → *name mangling*: o Python renomeia para `_Classe__atributo`, dificultando o acesso acidental.
- **Encapsulamento**: expor operações com sentido de negócio (`depositar`, `sacar`) em vez de entregar os dados
  crus. Uma conta bancária não deveria permitir `conta.saldo = 0`.

| Arquivo | Assunto |
| --- | --- |
| [`ocultamento_encapsulamento.py`](ocultamento_encapsulamento.py) | Atributos com `_`, getters/setters clássicos e métodos `depositar`/`sacar` |
| [`ocultamento_encapsulamento_decorator.py`](ocultamento_encapsulamento_decorator.py) | `@property` e `@atributo.setter` (forma pythônica) |

## Correções em relação aos slides

- `get_numero_conta` não tinha `return`.
- `self._ numero_conta` (com espaço) era um erro de digitação.
- Em `@property saldo`, o setter foi declarado como `@titular.setter`.
- Na versão final **não existe setter para saldo**: ele só muda via `depositar()`/`sacar()`.

## O que foi modernizado

- `@property` no lugar de `get_x()`/`set_x()` (a versão com `get_`/`set_` fica só para comparação).
- Validação nos métodos (valor positivo, saldo suficiente) levantando `ValueError`.
- Valores monetários formatados com f-string.
