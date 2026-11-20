"""Formas de usar o for."""

print("a) range(0, 10): de 0 a 9, de 1 em 1")
for contador in range(0, 10):
    print(contador, end=" ")

print("\n\nb) range(0, 20, 2): de 0 a 18, de 2 em 2 (o 20 não entra)")
for contador in range(0, 20, 2):
    print(contador, end=" ")

print("\n\nc) range(10, 0, -3): contagem regressiva")
for contador in range(10, 0, -3):
    print(contador, end=" ")

print("\n\nd) Percorrendo uma lista (colchetes, sem range)")
for primo in [2, 3, 5, 7, 11, 13, 17, 19]:
    print(primo, end=" ")

print("\n\ne) enumerate: índice e valor ao mesmo tempo")
for indice, letra in enumerate("Rio"):
    print(f"{indice} -> {letra}")
