"""Desvio condicional simples: soma dois números e só exibe se o resultado for maior que 10."""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2

if soma > 10:
    print(f"A soma dos números inseridos é {soma}")
