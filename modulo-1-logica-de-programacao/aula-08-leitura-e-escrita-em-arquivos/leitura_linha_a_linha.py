"""Leitura linha a linha.

Cada palavra está salva com \\n no final e o print() também acrescenta um \\n,
por isso as linhas aparecem com uma linha em branco entre elas.
"""

from pathlib import Path

ARQUIVO = Path(__file__).parent / "palavras.txt"

print("--- Todas as linhas (com \\n) ---")
with open(ARQUIVO, encoding="utf-8") as arquivo:
    for linha in arquivo:  # o próprio arquivo é iterável
        print("Linha capturada:", linha)

print("--- Uma linha de cada vez com readline() ---")
with open(ARQUIVO, encoding="utf-8") as arquivo:
    linha = arquivo.readline()
    print("Única linha capturada:", linha)
    linha = arquivo.readline()  # a próxima linha
    print("Única linha capturada:", linha)

    # strip() remove espaços e quebras de linha das pontas.
    linha = linha.strip()
    print("Sem o \\n:", linha)

print("--- Sem linhas em branco: end='' ---")
with open(ARQUIVO, encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha, end="")
