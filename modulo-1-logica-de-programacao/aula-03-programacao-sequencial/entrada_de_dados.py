"""Entrada de dados com input(): o retorno é sempre uma str."""

nome = input("Digite o seu nome: ")
numero = input("Digite um número: ")

print(f"Nome: {nome} ({type(nome).__name__})")
print(f"Número: {numero} ({type(numero).__name__})")

# Sem conversão, "+" concatena textos em vez de somar:
print(f"{numero} + {numero} = {numero + numero}")

# Com conversão, o "+" soma de verdade:
numero_inteiro = int(numero)
print(f"{numero_inteiro} + {numero_inteiro} = {numero_inteiro + numero_inteiro}")

# Outras conversões: int(), float(), bool(), str()
