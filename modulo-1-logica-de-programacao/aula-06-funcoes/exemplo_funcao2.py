"""Função com passagem de argumentos.

`nome`, na definição, é o PARÂMETRO; o valor enviado na chamada é o ARGUMENTO.
"""


def saudacao(nome: str) -> None:
    print(f"Olá, {nome}!")


def calcular_media(n1: float, n2: float, nome: str) -> None:
    media = (n1 + n2) / 2
    print(f"Aluno(a): {nome} - Média: {media}")


if __name__ == "__main__":
    print("Exemplo Função 2:")
    nome_completo = input("Informe o seu nome completo: ")
    nota1 = float(input(f"Informe a Nota 1 de {nome_completo}: "))
    nota2 = float(input(f"Informe a Nota 2 de {nome_completo}: "))

    saudacao(nome_completo)
    calcular_media(nota1, nota2, nome_completo)
    print("---FIM---")
