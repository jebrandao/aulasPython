"""from pacote.modulo import funcoes: importa apenas as funções necessárias."""

from util.teclado import ler_float, ler_int, ler_str

nome = ler_str("Qual o seu nome? ")
idade = ler_int("Qual a sua idade? ")
salario = ler_float("Qual o seu salário? ")

print(f"\nNome inserido: {nome}")
print(f"Idade inserida: {idade}")
print(f"Salário inserido: R$ {salario:,.2f}")
