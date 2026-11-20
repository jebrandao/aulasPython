"""Recursos do módulo math: raiz quadrada, potência e pi."""

import math

raiz = math.sqrt(16)
print(raiz)  # 4.0
print(type(raiz))  # <class 'float'>

potencia = math.pow(3, 4)
print(potencia)  # 81.0 (math.pow sempre devolve float)

# Para inteiros, o operador ** é mais simples e mantém o tipo int:
print(3**4)  # 81

numero_pi = math.pi
print(numero_pi)
