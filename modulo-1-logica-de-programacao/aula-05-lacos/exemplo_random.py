"""Sorteio de números com o módulo padrão random."""

import random

# randint inclui os dois extremos: sorteia de 1 a 10.
print(random.randint(1, 10))

# randrange funciona como range(): o valor final NÃO entra. Para sortear de 1 a 10, use (1, 11).
print(random.randrange(1, 11))

# Outras utilidades:
frutas = ["maçã", "uva", "banana"]
print(random.choice(frutas))  # um item aleatório
random.shuffle(frutas)  # embaralha a lista no lugar
print(frutas)
