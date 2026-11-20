# Aula 05 – Programação com laços

Laço (estrutura de repetição): um bloco executa várias vezes **enquanto** uma condição for verdadeira.

| Arquivo | Assunto |
| --- | --- |
| [`laco_while.py`](laco_while.py) | `while`: valor inicial, teste e incremento ficam separados |
| [`laco_for.py`](laco_for.py) | `for` + `range()` reúne os três itens |
| [`laco_for_variacoes.py`](laco_for_variacoes.py) | `range` com início/fim/passo, listas, `enumerate` |
| [`laco_break_while.py`](laco_break_while.py) / [`laco_break_for.py`](laco_break_for.py) | `break` interrompe o laço inteiro |
| [`laco_continue_while.py`](laco_continue_while.py) / [`laco_continue_for.py`](laco_continue_for.py) | `continue` pula só o ciclo atual (e a armadilha do laço infinito) |
| [`exemplo_random.py`](exemplo_random.py) | Sorteio com o módulo `random` |
| [`exercicio_break_continue.py`](exercicio_break_continue.py) | Jogo de adivinhação (gabarito + upgrade com sorteio) |

## Exercícios

- [`exercicios/lista_while.py`](exercicios/lista_while.py) – somente `while`
- [`exercicios/lista_for.py`](exercicios/lista_for.py) – somente `for`

## O que foi modernizado

- `contador += 1` em vez de `contador = contador + 1`.
- `for ... else`: o `else` do laço só executa se o laço terminou **sem** `break` (usado no jogo de adivinhação).
- Código morto removido (instruções após `break`/`continue` nunca executam).
- O jogo usa `random.randint(1, 20)` (inclui os dois extremos), que é mais claro que `randrange(1, 21)`.

> Atenção: o slide da aula pede para tirar o incremento de dentro do `if` ao usar `continue` com `while`,
> senão o laço fica infinito. A versão deste repositório já mostra a forma correta.
