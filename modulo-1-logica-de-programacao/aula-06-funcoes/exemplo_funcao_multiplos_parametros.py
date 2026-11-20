"""Funções com quantidade variável de parâmetros (*args)."""


def somar_tres(n1: float, n2: float, n3: float) -> float:
    """Limitada: só aceita exatamente 3 números."""
    return n1 + n2 + n3


def somar(*numeros: float) -> float:
    """O * agrupa todos os argumentos posicionais em uma tupla chamada numeros."""
    total = 0
    for numero in numeros:  # laço para percorrer todos os parâmetros
        total += numero
    return total


if __name__ == "__main__":
    print(somar_tres(1, 1, 1))  # 3
    print(somar(1, 1, 1))  # 3
    print(somar(1, 1, 1, 1, 1, 1, 1))  # 7
    print(somar())  # 0

    # Atalho da biblioteca padrão: sum() recebe um iterável.
    print(sum((1, 1, 1, 1, 1, 1, 1)))  # 7

    # Parâmetros nomeados variáveis: **kwargs (extra)
    def exibir(**dados: object) -> None:
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    exibir(nome="Ana", idade=20)
