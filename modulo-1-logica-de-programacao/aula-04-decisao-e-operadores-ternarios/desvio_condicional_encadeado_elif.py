"""Mesmo problema da versão encadeada, agora com elif (substitui um else que contém um if).

Regra: a última alternativa de um desvio condicional deve ser sempre else, nunca elif.
"""

num = int(input("Digite um número: "))

if num < 100:
    print(f"{num} está abaixo de 100.")
elif num <= 200:
    print(f"{num} está entre 100 e 200.")
else:
    print(f"{num} está acima de 200.")
