"""Escrita em arquivo: modos "w" (sobrescreve) e "a" (acrescenta)."""

from pathlib import Path

ARQUIVO = Path(__file__).parent / "palavras.txt"  # sempre ao lado deste script

# "w" cria o arquivo ou SOBRESCREVE o que já existe.
# Sem "\n" as palavras ficam concatenadas: bananamelanciaabacate
with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    print(arquivo)  # mostra nome, modo e codificação
    arquivo.write("banana")
    arquivo.write("melancia")
    arquivo.write("abacate")
# Ao sair do bloco with, o arquivo é fechado automaticamente (não precisa de close()).
print("Conteúdo após o 1º write:", ARQUIVO.read_text(encoding="utf-8"))

# Abrir de novo com "w" apaga tudo e começa do zero.
with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    arquivo.write("banana")
print("Conteúdo após sobrescrever:", ARQUIVO.read_text(encoding="utf-8"))

# Agora uma palavra por linha (\n):
frutas = ["banana", "melancia", "abacate", "morango", "abacaxi", "amora"]
with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    for fruta in frutas:
        arquivo.write(f"{fruta}\n")

# "a" (append) acrescenta ao final sem apagar:
with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
    arquivo.write("caju\n")

print("\nConteúdo final:")
print(ARQUIVO.read_text(encoding="utf-8"))

# Restaura o arquivo de exemplo usado nas demais aulas (sem "caju").
ARQUIVO.write_text("".join(f"{fruta}\n" for fruta in frutas), encoding="utf-8")
