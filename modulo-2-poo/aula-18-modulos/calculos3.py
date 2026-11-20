"""from modulo import *: traz TUDO. Deve ser evitado, principalmente em módulos grandes."""

from calculadora import *  # noqa: F403

print(somar(10, 20))  # noqa: F405
print(subtrair(15, 40))  # noqa: F405
print(multiplicar(3, 5))  # noqa: F405
print(numero_importante)  # noqa: F405
