"""Leitura completa com read() e o "ponteiro de fluxo"."""

from pathlib import Path

ARQUIVO = Path(__file__).parent / "palavras.txt"

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:  # noqa: UP015  ("r" é o padrão; explícito aqui por didática)
    print("1ª leitura:")
    print(arquivo.read())

    # O ponteiro de fluxo agora está no FINAL do arquivo, então não há mais o que ler:
    print("2ª leitura (vazia):")
    print(repr(arquivo.read()))

    arquivo.seek(0)  # volta o ponteiro ao início, sem precisar fechar e reabrir
    print("Após seek(0):")
    print(arquivo.read())
