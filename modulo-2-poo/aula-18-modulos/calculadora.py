"""Módulo próprio: uma variável e algumas funções simples para serem importadas."""

numero_importante = 100


def somar(n1: float, n2: float) -> float:
    return n1 + n2


def subtrair(n1: float, n2: float) -> float:
    return n1 - n2


def multiplicar(n1: float, n2: float) -> float:
    return n1 * n2


# Só executa quando ESTE arquivo é rodado diretamente, não quando é importado.
if __name__ == "__main__":
    print("\n--- Utilizando o Arquivo Python calculadora.py ---\n")
