"""Variáveis: o tipo é definido pelo valor inicial."""

pais = "Brasil"
numero = 10
casado = True

print(pais, type(pais))
print(numero, type(numero))
print(casado, type(casado))

nome = input("Informe o seu nome: ")  # sem conversão: nome é sempre texto
salario = float(input("Informe o seu salário: "))  # str -> float
idade = int(input("Informe a sua idade: "))  # str -> int

print(type(nome), type(salario), type(idade))
