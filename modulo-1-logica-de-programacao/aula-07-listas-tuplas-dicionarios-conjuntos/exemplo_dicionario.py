"""Dicionários: pares chave/valor."""

verbos = {
    "pular": "elevar-se do chão por impulso dos pés e das pernas",
    "cair": "ir ao chão",
    "devolver": "entregar ou enviar de volta",
}

print(verbos)
print(type(verbos))
print(verbos["cair"])  # ir ao chão

carro = {
    "fabricante": "VW",
    "modelo": "Fusca",
    "cor": "Verde",
    "ano": 1975,
    "donos": ["João", "José", "Maria"],  # o valor pode ser uma lista
}
print(carro)
print(carro["modelo"])  # Fusca

print("\n--- Valores que são listas ---")
print(carro["donos"])
carro["donos"].append("Ana")  # acrescenta à lista dentro do dicionário
print(carro["donos"][1])  # José

print("\n--- Adicionar, alterar, remover ---")
carro["km"] = 115000  # chave nova
carro["km"] = 173000  # chave existente: altera o valor
print(carro)

carro.update({"cor": "Amarelo"})  # outra forma de alterar (ou adicionar)
print(carro)

del carro["km"]  # remove chave e valor
removido = carro.pop("cor")  # remove e devolve o valor
print(carro)
print(f"Removido: {removido}")

print("\n--- Consultas ---")
print(carro.keys())  # só as chaves
print(carro.values())  # só os valores
print(carro.items())  # pares (chave, valor)
print(carro.get("fabricante"))  # VW
print(carro.get("cor", "Azul"))  # chave inexistente: devolve o padrão, sem KeyError
print(len(carro))

for chave, valor in carro.items():
    print(f"{chave}: {valor}")

# Mesclar dicionários (Python 3.9+)
extras = {"cor": "Vermelho", "km": 90000}
carro = carro | extras
print(carro)

carro.clear()
print(carro)  # {}
