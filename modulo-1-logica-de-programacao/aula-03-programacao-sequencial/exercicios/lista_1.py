"""Lista 1 de exercícios de programação sequencial – resolução sugerida.

Execute e escolha o número do exercício: python lista_1.py
"""

import math


def ex01() -> None:
    """Nome completo e sexo, depois exibe os dados informados."""
    nome = input("Informe o seu nome completo: ")
    sexo = input("Informe o seu sexo: ")
    print(f"\nNome: {nome}\nSexo: {sexo}")


def ex02() -> None:
    """Quatro inteiros: soma e produto."""
    n1 = int(input("1º valor inteiro: "))
    n2 = int(input("2º valor inteiro: "))
    n3 = int(input("3º valor inteiro: "))
    n4 = int(input("4º valor inteiro: "))
    print(f"Adição: {n1 + n2 + n3 + n4}")
    print(f"Multiplicação: {n1 * n2 * n3 * n4}")


def ex03() -> None:
    """Dólares para reais (US$ 1,00 = R$ 3,80)."""
    cotacao = 3.80
    dolares = float(input("Valor em dólares (US$): "))
    print(f"US$ {dolares:.2f} equivalem a R$ {dolares * cotacao:.2f}")


def ex04() -> None:
    """Antecessor e sucessor."""
    numero = int(input("Informe um número inteiro: "))
    print(f"Antecessor: {numero - 1}")
    print(f"Sucessor: {numero + 1}")


def ex05() -> None:
    """Salário com aumento de 15%."""
    salario = float(input("Salário atual (R$): "))
    print(f"Salário com 15% de aumento: R$ {salario * 1.15:.2f}")


def ex06() -> None:
    """Fahrenheit para Celsius: c = (f - 32) * 5 / 9."""
    fahrenheit = float(input("Temperatura em °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.1f} °F equivalem a {celsius:.1f} °C")


def ex07() -> None:
    """Média aritmética de 3 números."""
    n1 = float(input("1º número: "))
    n2 = float(input("2º número: "))
    n3 = float(input("3º número: "))
    print(f"Média aritmética: {(n1 + n2 + n3) / 3:.2f}")


def ex08() -> None:
    """Litros gastos em uma viagem."""
    distancia = float(input("Distância da viagem (km): "))
    consumo = float(input("Consumo médio do automóvel (km/l): "))
    print(f"Serão gastos {distancia / consumo:.2f} litros de combustível.")


def ex09() -> None:
    """Número, quadrado e raiz quadrada."""
    numero = float(input("Informe um número (não negativo): "))
    print(f"Número: {numero}")
    print(f"Quadrado: {numero**2}")
    print(f"Raiz quadrada: {math.sqrt(numero):.4f}")


def ex10() -> None:
    """Prestação em atraso: valor + (valor * (taxa / 100) * dias)."""
    valor = float(input("Valor da prestação (R$): "))
    taxa = float(input("Taxa de juros diária (%): "))
    dias = int(input("Dias em atraso: "))
    total = valor + (valor * (taxa / 100) * dias)
    print(f"Valor a pagar: R$ {total:.2f}")


EXERCICIOS = {
    1: ex01,
    2: ex02,
    3: ex03,
    4: ex04,
    5: ex05,
    6: ex06,
    7: ex07,
    8: ex08,
    9: ex09,
    10: ex10,
}


def main() -> None:
    numero = int(input(f"Qual exercício executar (1-{len(EXERCICIOS)})? "))
    EXERCICIOS[numero]()


if __name__ == "__main__":
    main()
