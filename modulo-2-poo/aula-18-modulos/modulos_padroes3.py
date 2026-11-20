"""from ... import *: importa todos os nomes públicos dos módulos. Evite."""

from math import *  # noqa: F403
from random import *  # noqa: F403

print(f"Sorteio de um número entre 1 e 10: {randint(1, 10)}")  # noqa: F405
print(f"Valor de PI: {pi}")  # noqa: F405
