"""Função com retorno: calcular_media() devolve o valor para quem a chamou."""


def saudacao(nome: str) -> None:
    print(f"Olá, {nome}!")


def calcular_media(n1: float, n2: float) -> float:
    return (n1 + n2) / 2


def situacao(media_final: float, nome: str) -> None:
    resultado = "Aprovado" if media_final >= 7 else "Reprovado"
    print(f"Nome: {nome} - Média Final: {media_final} - Situação: {resultado}")


if __name__ == "__main__":
    print("Exemplo Função 3:")
    nome_completo = input("Informe o seu nome completo: ")
    nota1 = float(input(f"Informe a Nota 1 de {nome_completo}: "))
    nota2 = float(input(f"Informe a Nota 2 de {nome_completo}: "))

    saudacao(nome_completo)
    media = calcular_media(nota1, nota2)  # o valor retornado é guardado em media
    situacao(media, nome_completo)
    print("---FIM---")
