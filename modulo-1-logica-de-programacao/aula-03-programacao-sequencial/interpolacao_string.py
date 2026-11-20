"""Interpolação de strings: quatro formas de misturar texto e variáveis."""

nome = input("Digite o seu primeiro nome: ")
idade = int(input("Digite sua idade: "))

print("\n1) Vírgulas no print (insere espaços automaticamente)")
print("Olá,", nome, "!")
print("Caramba", nome, "! Você tem", idade, "anos? Nem parece.")

print("\n2) str.format() (Python 2.6+, ainda comum em código antigo)")
print("Olá, {}!".format(nome))
print("Caramba {}! Você tem {} anos? Nem parece.".format(nome, idade))

print("\n3) f-string (Python 3.6+) -> FORMA RECOMENDADA")
print(f"Olá, {nome}!")
print(f"Caramba {nome}! Você tem {idade} anos? Nem parece.")
print(f"Nome em minúsculas: {nome.lower()} | em maiúsculas: {nome.upper()}")
print(f"Em 10 anos você terá {idade + 10} anos.")  # aceita expressões
print(f"{nome=}  {idade=}")  # '=' mostra nome e valor (ótimo para depurar)

print("\n4) Operador % (estilo C, legado)")
print("Olá, %s!" % nome)
print("Caramba %s! Você tem %d anos? Nem parece." % (nome, idade))
