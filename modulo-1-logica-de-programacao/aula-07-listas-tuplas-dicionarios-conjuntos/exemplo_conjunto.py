"""Conjuntos (sets): coleções sem ordem e sem itens repetidos."""

nomes = {"João", "Maria", "Pedro", "José", "Ana"}
print(type(nomes))
print(nomes)  # a ordem pode variar a cada execução

nomes.add("Jorge")
print(nomes)

nomes.remove("Jorge")  # KeyError se não existir; discard() não gera erro
print(nomes)

nomes.add("Maria")  # repetido: ignorado
print(nomes)

nomes2 = {"Vanessa", "Jéssica", "Maria", "Ana", "Simone"}
print(nomes2)

print("União:", nomes.union(nomes2))  # sem repetições
print("Interseção:", nomes.intersection(nomes2))
print("Diferença (só em nomes):", nomes.difference(nomes2))

# Operadores equivalentes:
print(nomes | nomes2, nomes & nomes2, nomes - nomes2)

# Uso clássico: remover duplicados de uma lista.
com_repetidos = [3, 1, 3, 2, 1]
print(sorted(set(com_repetidos)))  # [1, 2, 3]

vazio = set()  # {} criaria um dicionário vazio
print(type(vazio), type({}))
