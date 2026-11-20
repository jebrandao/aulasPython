"""Lista 1 de exercícios de decisão e operadores ternários – resolução sugerida.

Execute e escolha o número do exercício: python lista_1.py
"""


def ex01() -> None:
    """Se o número for maior que 20, exibe a metade; senão, exibe o próprio número."""
    numero = float(input("Informe um número: "))
    print(numero / 2 if numero > 20 else numero)


def ex02() -> None:
    """Qual é a capital do Brasil?"""
    resposta = input("Qual é a capital do Brasil? ").strip().lower()
    print("Resposta certa!" if resposta in {"brasília", "brasilia"} else "Resposta errada!")


def ex03() -> None:
    """Par ou ímpar."""
    numero = int(input("Informe um número inteiro: "))
    print(f"{numero} é {'par' if numero % 2 == 0 else 'ímpar'}")


def ex04() -> None:
    """Exibe o valor se for divisível por 4 e por 5."""
    numero = int(input("Informe um número inteiro: "))
    if numero % 4 == 0 and numero % 5 == 0:
        print(numero)
    else:
        print("Valor não é divisível por 4 e 5")


def ex05() -> None:
    """Média de 4 notas: aprovado se média >= 5."""
    notas = [float(input(f"Nota {i}: ")) for i in range(1, 5)]
    media = sum(notas) / len(notas)
    situacao = "APROVADO" if media >= 5 else "REPROVADO"
    print(f"Média: {media:.2f} - {situacao}")


def ex06() -> None:
    """Diferença entre o maior e o menor de dois valores."""
    a = int(input("1º valor: "))
    b = int(input("2º valor: "))
    print(f"Diferença entre o maior e o menor: {max(a, b) - min(a, b)}")


def ex07() -> None:
    """Módulo (valor absoluto) de um número."""
    numero = int(input("Informe um número inteiro: "))
    print(f"Módulo: {abs(numero)}")


def ex08() -> None:
    """O número está entre 1 e 10?"""
    numero = int(input("Informe um número inteiro: "))
    if 1 <= numero <= 10:  # comparação encadeada
        print(f"{numero} está na faixa de 1 a 10.")
    else:
        print(f"{numero} NÃO está na faixa de 1 a 10.")


def ex09() -> None:
    """Positivo, negativo ou nulo."""
    numero = float(input("Informe um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Nulo")


def ex10() -> None:
    """O segundo número é divisor do primeiro?"""
    a = int(input("1º número inteiro: "))
    b = int(input("2º número inteiro: "))
    if b != 0 and a % b == 0:
        print(f"{b} é divisor de {a}.")
    else:
        print(f"{b} NÃO é divisor de {a}.")


def ex11() -> None:
    """Algarismo das centenas de um número de 3 algarismos."""
    numero = int(input("Informe um número inteiro de 3 algarismos: "))
    if 100 <= abs(numero) <= 999:
        print(f"Algarismo das centenas: {abs(numero) // 100}")
    else:
        print("O número não tem 3 algarismos.")


def ex12() -> None:
    """Maior e menor entre 5 números."""
    numeros = [int(input(f"{i}º número: ")) for i in range(1, 6)]
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}")


def ex13() -> None:
    """Três valores em ordem crescente."""
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print("Ordem crescente:", *sorted([a, b, c]))


EXERCICIOS = {
    1: ex01, 2: ex02, 3: ex03, 4: ex04, 5: ex05, 6: ex06, 7: ex07,
    8: ex08, 9: ex09, 10: ex10, 11: ex11, 12: ex12, 13: ex13,
}  # fmt: skip


def main() -> None:
    numero = int(input(f"Qual exercício executar (1-{len(EXERCICIOS)})? "))
    EXERCICIOS[numero]()


if __name__ == "__main__":
    main()
