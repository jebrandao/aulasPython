"""Formatação de números int. O valor da variável não muda: só a exibição."""

num1 = 6
num2 = 382

print("--- .format() (legado) ---")
print("num1: {:d}".format(num1))  # apenas int
print("num1: {:7d}".format(num1))  # largura 7
print("num2: {:7d}".format(num2))
print("num1: {:07d}".format(num1))  # largura 7 com zeros à esquerda
print("num2: {:07d}".format(num2))

print("\n--- f-string (recomendado) ---")
print(f"num1: {num1:d}")
print(f"num1: {num1:7d}")
print(f"num2: {num2:7d}")
print(f"num1: {num1:07d}")
print(f"num2: {num2:07d}")
print(f"1 milhão: {1_000_000:,}")  # separador de milhar; o literal 1_000_000 é válido
