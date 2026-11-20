"""Sequências de escape em strings."""

frase1 = 'Sequência de "Escape"'  # aspas duplas dentro de aspas simples dispensam o \"
# Mesmo resultado com \" dentro de aspas duplas (o fmt: skip impede o formatador de trocar as aspas):
frase1_com_escape = "Sequência de \"Escape\""  # fmt: skip
print(frase1)
print(frase1_com_escape)

frase2 = "C:\\Meus Documentos\\foto1.jpg"  # \\ vira uma barra
print(frase2)

# Raw string (prefixo r): a barra invertida é tratada literalmente. Ótimo para caminhos e regex.
frase2_raw = r"C:\Meus Documentos\foto1.jpg"
print(frase2_raw)
assert frase2 == frase2_raw

frase3 = "Bom dia!\nJá nasceu o sol na fazendinha!"  # \n = nova linha
print(frase3)

print("Nome\tIdade\nAna\t20\nBia\t22")  # \t = tabulação

# Texto com várias linhas: aspas triplas dispensam o \n
poema = """Rio de Janeiro
Cidade maravilhosa"""
print(poema)
