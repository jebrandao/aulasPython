"""Sem tratamento de exceções: experimente digitar 9 (índice inexistente) e depois "abc".

Observe com atenção as mensagens de erro (IndexError e ValueError) que o Python exibe.
"""

nomes = ["Carlos", "Matheus", "Maria", "Jéssica", "Ana"]
numero = int(input("Informe um número para que seja exibido o nome correspondente da lista: "))
print(f"Nome encontrado na posição {numero} da lista: {nomes[numero]}")
