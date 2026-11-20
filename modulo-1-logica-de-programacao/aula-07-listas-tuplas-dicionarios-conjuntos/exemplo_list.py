"""Listas dinâmicas: criação, consulta, inclusão, remoção, ordenação."""

frutas = ["Maçã", "Uva", "Banana", "Manga", "Laranja", "Limão"]

print(frutas)
print(type(frutas))
print("Conteúdo do índice 1:", frutas[1])
print("Último item:", frutas[-1])
print("Total de frutas armazenadas:", len(frutas))
print("Temos Manga?", "Manga" in frutas)
print("Temos Morango?", "Morango" in frutas)

print("\n--- Incluindo e removendo ---")
frutas.append("Morango")  # adiciona ao final
print(frutas)
print("Índice para Laranja:", frutas.index("Laranja"))

frutas.remove("Uva")  # remove pelo valor
print(frutas)
print("Índice para Laranja agora:", frutas.index("Laranja"))

removida = frutas.pop(3)  # remove pelo índice e devolve o item (del frutas[3] só remove)
print(f"\nQuem foi removido? {removida}")
print(frutas)

frutas.insert(2, "Abacaxi")  # cria a posição 2, empurrando os demais
print("\nApós insert:", frutas)
print("Índice do Abacaxi:", frutas.index("Abacaxi"))

frutas[3] = "Acerola"  # altera o valor da posição, sem criar nova posição
print("Após alterar o índice 3:", frutas)
print(f"Total de itens na lista: {len(frutas)}")

print("\n--- Consulta e contagem ---")
fruta = input("Digite uma fruta: ").strip()
if fruta in frutas:
    print(f"{fruta} existe na lista frutas")
else:
    print(f"{fruta} não existe na lista frutas")

print('Quantidade de "Laranja":', frutas.count("Laranja"))
print('Quantidade de "Uva":', frutas.count("Uva"))

print("\n--- reverse e sort ---")
frutas.reverse()  # inverte a ordem (modifica a própria lista)
print(frutas)
frutas.sort()  # ordem alfabética (modifica a própria lista)
print(frutas)
print(sorted(frutas, reverse=True))  # sorted() devolve uma NOVA lista; a original não muda
print(frutas)
