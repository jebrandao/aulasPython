# Aula 15 – POO: classe abstrata

Uma **classe abstrata** serve de modelo para as subclasses e **não deve ser instanciada**.
Um **método abstrato** não tem implementação na superclasse: **obriga** cada subclasse a implementá-lo.

Passos da aula (e o que cada um demonstra):

1. Superclasse comum → é possível instanciar `Pessoa`.
2. `class Pessoa(ABC)` **sem** método abstrato → ainda é possível instanciar.
3. Método concreto na superclasse (`exibir_matricula_nome`) → herdado normalmente.
4. `@abstractmethod` na superclasse → `Pessoa()` e subclasses que **não** implementem o método passam a gerar `TypeError`.

| Arquivo | Assunto |
| --- | --- |
| [`classe_abstrata.py`](classe_abstrata.py) | Versão final, com testes dos erros esperados |

## O que foi modernizado

- `try/except TypeError` para **mostrar** o erro de instanciar uma classe abstrata em vez de parar o programa.
- Uma subclasse propositalmente incompleta (`Visitante`) demonstra a obrigação de sobrescrever.
- `@abstractmethod` junto com `@property` para uma propriedade abstrata (`papel`).
