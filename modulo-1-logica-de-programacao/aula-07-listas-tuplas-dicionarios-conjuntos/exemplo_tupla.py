"""Tuplas: listas imutáveis."""

sudeste = ("RJ", "ES", "SP", "MG")
print(type(sudeste))
print(sudeste)

print(sudeste[0])  # RJ
print(sudeste[-1])  # MG (o último)
print(sudeste[:2])  # ('RJ', 'ES')  -> índices 0 e 1
print(sudeste[1:3])  # ('ES', 'SP')  -> índices 1 e 2
print(sudeste[::2])  # ('RJ', 'SP')  -> de 2 em 2

print(len(sudeste))  # 4
print(sudeste.index("SP"))  # 2
print(sudeste.count("SP"))  # 1

# Tuplas são imutáveis:
try:
    sudeste[0] = "BA"  # type: ignore[index]
except TypeError as erro:
    print(f"Erro esperado: {erro}")

# Desempacotamento: muito usado para retornar vários valores de uma função.
rj, es, sp, mg = sudeste
print(rj, es, sp, mg)
