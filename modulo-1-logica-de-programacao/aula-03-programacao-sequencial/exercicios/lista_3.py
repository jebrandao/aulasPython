"""Lista 3 de exercícios de programação sequencial – resolução sugerida.

Execute e escolha o número do exercício: python lista_3.py
"""

import math


def ex01() -> None:
    """Área do círculo: pi * r²."""
    raio = float(input("Raio do círculo: "))
    print(f"Área: {math.pi * raio**2:.2f}")


def ex02() -> None:
    """Salário líquido do professor."""
    valor_hora = float(input("Valor da hora-aula (R$): "))
    horas = float(input("Horas trabalhadas no mês: "))
    inss = float(input("Percentual de desconto do INSS (%): "))
    bruto = valor_hora * horas
    desconto = bruto * inss / 100
    print(f"Salário bruto: R$ {bruto:.2f}")
    print(f"Desconto INSS: R$ {desconto:.2f}")
    print(f"Salário líquido: R$ {bruto - desconto:.2f}")


def ex03() -> None:
    """Primeiro valor com acréscimo de 30% e segundo com desconto de 25%."""
    v1 = float(input("1º valor: "))
    v2 = float(input("2º valor: "))
    print(f"1º valor com 30% de acréscimo: {v1 * 1.30:.2f}")
    print(f"2º valor com 25% de desconto: {v2 * 0.75:.2f}")


def ex04() -> None:
    """Média ponderada com pesos 1, 2, 3 e 4."""
    notas = [float(input(f"Número {i}: ")) for i in range(1, 5)]
    pesos = [1, 2, 3, 4]
    media = sum(n * p for n, p in zip(notas, pesos, strict=True)) / sum(pesos)
    print(f"Média ponderada: {media:.2f}")


def ex05() -> None:
    """Volume da lata de óleo: pi * r² * h."""
    raio = float(input("Raio da lata: "))
    altura = float(input("Altura da lata: "))
    print(f"Volume: {math.pi * raio**2 * altura:.2f}")


def ex06() -> None:
    """Troca de valores entre duas variáveis."""
    a = input("Valor de a: ")
    b = input("Valor de b: ")
    a, b = b, a  # troca sem variável auxiliar (desempacotamento de tupla)
    print(f"Após a troca: a = {a} e b = {b}")


def ex07() -> None:
    """Hipotenusa de um triângulo retângulo."""
    c1 = float(input("Cateto 1: "))
    c2 = float(input("Cateto 2: "))
    print(f"Hipotenusa: {math.hypot(c1, c2):.2f}")  # equivale a sqrt(c1² + c2²)


def ex08() -> None:
    """Perímetro, área e diagonal de um retângulo."""
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print(f"Perímetro: {2 * (base + altura):.2f}")
    print(f"Área: {base * altura:.2f}")
    print(f"Diagonal: {math.hypot(base, altura):.2f}")


def ex09() -> None:
    """10º termo de uma PA: a1 + (n - 1) * r."""
    razao = float(input("Razão da PA: "))
    primeiro = float(input("1º termo: "))
    print(f"10º termo: {primeiro + 9 * razao}")


def ex10() -> None:
    """5º termo de uma PG: a1 * q^(n - 1)."""
    razao = float(input("Razão da PG: "))
    primeiro = float(input("1º termo: "))
    print(f"5º termo: {primeiro * razao**4}")


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
