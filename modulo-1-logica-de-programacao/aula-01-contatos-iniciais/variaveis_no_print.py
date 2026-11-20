"""Variáveis dentro do print() e tipagem dinâmica."""

regiao = "Região Norte"
total = 7
print(type(regiao))  # <class 'str'>
print(type(total))  # <class 'int'>

print(regiao, total, "Estados")
print(regiao, total, "Estados", sep="-", end=".\n")

# Variáveis são dinâmicas: podem receber valores de outros tipos depois.
regiao = "Região Sul"
total = 3
print(regiao, total, "Estados", sep=";")

total = "três"  # agora total é str
print(type(total))
