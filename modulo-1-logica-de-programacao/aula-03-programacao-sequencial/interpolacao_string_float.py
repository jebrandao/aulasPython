"""Formatação de números float (versão .format() e versão f-string lado a lado)."""

valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349
valor4 = 0.7536

print("--- .format() (legado) ---")
print("Valor 1: {:f}".format(valor1))  # float "cru"
print("Valor 1: {:.2f}".format(valor1))  # 2 casas decimais
print("Valor 2: {:10.2f}".format(valor2))  # largura total 10, 2 decimais
print("Valor 2: {:010.2f}".format(valor2))  # idem, completando com zeros
print("Valor 2: {:,.2f}".format(valor2))  # separador de milhar

print("\n--- f-string (recomendado) ---")
print(f"Valor 1: {valor1:f}")
print(f"Valor 1: {valor1:.2f}")
print(f"Valor 2: {valor2:10.2f}")
print(f"Valor 2: {valor2:010.2f}")
print(f"Valor 3: {valor3:10.2f}")
print(f"Valor 2: {valor2:,.2f}")

print("\n--- Percentual, moeda e padrão brasileiro ---")
print(f"Valor 4: {valor4:.1%}")  # 0.7536 -> 75.4%

texto_valor2 = f"R$ {valor2:_.2f}"  # milhar com underline
print(f"Texto Valor 2: {texto_valor2}")

# Padrão brasileiro: troca "." por "," e "_" por ".". O translate faz tudo de uma vez,
# o que evita o problema de trocar uma vírgula que acabou de ser inserida.
para_brasil = str.maketrans({".": ",", "_": "."})
print(f"Texto Valor BR: {texto_valor2.translate(para_brasil)}")  # R$ 73.932,60
