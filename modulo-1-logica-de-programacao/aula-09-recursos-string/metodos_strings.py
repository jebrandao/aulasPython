"""Extra: métodos de string muito usados no dia a dia."""

frase = "  Python é uma linguagem versátil  "

print(f"[{frase.strip()}]")  # remove espaços das pontas
print(frase.upper())
print(frase.lower())
print(frase.title())

limpa = frase.strip()
print(limpa.replace("versátil", "poderosa"))
print(limpa.startswith("Python"), limpa.endswith("!"))
print(limpa.count("a"))  # quantas vezes "a" aparece
print(limpa.find("uma"))  # posição da primeira ocorrência (-1 se não achar)

palavras = limpa.split()  # separa por espaços -> lista
print(palavras)
print("-".join(palavras))  # junta a lista com um separador

print("123".isdigit(), "abc".isalpha(), "abc123".isalnum())
print("42".zfill(5))  # 00042
print(f"{'centro':^20}|{'esq':<10}|{'dir':>10}|")  # alinhamento em f-string
