"""Lendo as palavras de um arquivo para dentro de uma lista."""

from pathlib import Path

ARQUIVO = Path(__file__).parent / "palavras.txt"

# Forma didática, com laço:
palavras = []
with open(ARQUIVO, encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())
print(palavras)

# Forma compacta (compreensão de lista):
with open(ARQUIVO, encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo]
print(palavras)

# Atalho de pathlib: lê tudo e já separa por linhas.
palavras = ARQUIVO.read_text(encoding="utf-8").splitlines()
print(palavras)
print(f"Total de palavras: {len(palavras)}")
