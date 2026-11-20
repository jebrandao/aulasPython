"""Função básica, sem parâmetros e sem retorno."""


def saudacao() -> None:
    nome = input("Informe o seu nome: ")
    print(f"Olá, {nome}!")


if __name__ == "__main__":
    print("Exemplo Função 1:")
    saudacao()  # chamada para executar a função
    print("---FIM---")
