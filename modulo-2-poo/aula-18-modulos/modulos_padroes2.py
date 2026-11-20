"""from ... import ... as ...: importa só o necessário e permite apelidos."""

from math import pi
from math import pow as potencia  # cuidado: sem o apelido, esconderia o pow() embutido
from math import sqrt as raiz
from random import randint

print(f"Sorteio de um número entre 1 e 10: {randint(1, 10)}")
print(f"Valor de PI: {pi}")
print(f"5 elevado ao quadrado: {potencia(5, 2)}")
print(f"Raiz quadrada de 36: {raiz(36)}")
