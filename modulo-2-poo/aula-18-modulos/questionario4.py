"""from pacote.modulo import *: traz tudo do módulo. Evite."""

from util.teclado import *  # noqa: F403

nome = ler_str("Qual o seu nome? ")  # noqa: F405
idade = ler_int("Qual a sua idade? ")  # noqa: F405
salario = ler_float("Qual o seu salário? ")  # noqa: F405

print(f"\nNome inserido: {nome}")
print(f"Idade inserida: {idade}")
print(f"Salário inserido: R$ {salario:,.2f}")
