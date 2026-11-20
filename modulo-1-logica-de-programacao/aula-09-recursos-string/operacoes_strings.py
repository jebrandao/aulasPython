"""Operações com strings: indexação, fatiamento e busca."""

texto = "Rio de Janeiro"
print(texto)

print("\n--- Caracteres específicos ---")
print(texto[0])  # R
print(texto[1])  # i
print(texto[7])  # J

print("\n--- A partir do final ---")
print(texto[-1])  # o
print(texto[-2])  # r

print("\n--- Trechos [início:fim] (o fim NÃO entra) ---")
print(texto[:2])  # Ri
print(texto[:5])  # Rio d
print(texto[7:])  # Janeiro
print(texto[7:9])  # Ja

print("\n--- Passo [::n] ---")
print(texto[::2])  # Rod aer  (caractere sim, caractere não)
print(texto[::3])  # R  nr
print(texto[::4])  # Rdar
print(texto[::-1])  # orienaJ ed oiR (de trás para a frente)

print("\n--- Cada caractere ---")
for letra in texto:
    print(letra, end=" ")
print()

print("\n--- Busca com in ---")
print("a" in texto)  # True
print("b" in texto)  # False
print(" " in texto)  # True
print("Janeiro" in texto)  # True

print("\n--- Imutabilidade ---")
try:
    texto[0] = "r"  # type: ignore[index]
except TypeError as erro:
    print(f"Strings não podem ser alteradas: {erro}")
