"""Operadores aritméticos, relacionais e lógicos."""

a = 3
b = -4

print("--- Aritméticos ---")
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão (float): {a / b}")
print(f"Divisão inteira: {a // b}")  # arredonda para baixo: 3 // -4 = -1
print(f"Resto da divisão de 16 por a: {16 % a}")
print(f"Potência a**2: {a**2}")
print(f"Cálculos dentro do print: {a * b}")

print("\n--- Relacionais (= atribui, == compara) ---")
print(f"a == b: {a == b}")
print(f"a < 5: {a < 5}")
print(f"a > b: {a > b}")
print(f"a <= 3: {a <= 3}")
print(f"a >= 4: {a >= 4}")
print(f"a != b: {a != b}")

print("\n--- Lógicos ---")
logic1 = True
logic2 = False
print(type(logic1))
print(f"logic1: {logic1}")
print(f"not logic1: {not logic1}")
print(f"logic1 or logic2: {logic1 or logic2}")
print(f"logic1 and logic2: {logic1 and logic2}")

print("\n--- Tabela-verdade ---")
print(f"{'A':<6}{'B':<6}{'not A':<8}{'A and B':<10}{'A or B':<8}")
for x in (True, False):
    for y in (True, False):
        print(f"{x!s:<6}{y!s:<6}{(not x)!s:<8}{(x and y)!s:<10}{(x or y)!s:<8}")
