"""Lista de exercícios de laços – somente WHILE – resolução sugerida.

Execute e escolha o número do exercício: python lista_while.py
"""

import math


def ex01() -> None:
    """Números de 1 a 100."""
    n = 1
    while n <= 100:
        print(n)
        n += 1


def ex02() -> None:
    """Números de 100 até 1 (decrescente)."""
    n = 100
    while n >= 1:
        print(n)
        n -= 1


def ex03() -> None:
    """Quadrados dos inteiros de 15 a 200."""
    n = 15
    while n <= 200:
        print(f"{n}² = {n**2}")
        n += 1


def ex04() -> None:
    """Soma dos cem primeiros inteiros."""
    n = 1
    soma = 0
    while n <= 100:
        soma += n
        n += 1
    print(f"1 + 2 + ... + 100 = {soma}")


def ex05() -> None:
    """Tabuada de um número."""
    numero = int(input("Tabuada de qual número? "))
    i = 1
    while i <= 10:
        print(f"{numero} . {i} = {numero * i}")
        i += 1


def ex06() -> None:
    """Multiplica n por 3 sucessivamente enquanto o produto for menor que 250."""
    n = int(input("Informe n (<= 50): "))
    produto = n * 3
    while produto < 250:
        print(produto)
        produto *= 3


def ex07() -> None:
    """Números divisíveis por 4 menores que 200 (contador inicia em 1)."""
    n = 1
    while n < 200:
        if n % 4 == 0:
            print(n)
        n += 1


def ex08() -> None:
    """Ímpares de 0 a 20."""
    n = 0
    while n <= 20:
        if n % 2 != 0:
            print(n)
        n += 1


def ex09() -> None:
    """Soma dos pares de 0 a 500 (variando de 2 em 2)."""
    n = 0
    soma = 0
    while n <= 500:
        soma += n
        n += 2
    print(f"Soma dos pares de 0 a 500: {soma}")


def ex10() -> None:
    """Potências de 3 de 0 a 15: com math.pow e sem math.pow."""
    print("Com math.pow (devolve float):")
    e = 0
    while e <= 15:
        print(f"3 elevado à {e} = {math.pow(3, e):.0f}")
        e += 1

    print("\nSem math.pow (multiplicações sucessivas):")
    e = 0
    potencia = 1
    while e <= 15:
        print(f"3 elevado à {e} = {potencia}")
        potencia *= 3
        e += 1


def ex11() -> None:
    """Potência b^e sem usar math.pow nem o operador **."""
    b = float(input("Base: "))
    e = int(input("Expoente (inteiro >= 0): "))
    resultado = 1.0
    contador = 0
    while contador < e:
        resultado *= b
        contador += 1
    print(f"{b} elevado a {e} = {resultado}")


def ex12() -> None:
    """Lê reais até digitar -1; mostra maior, menor e média (sem contar o -1)."""
    maior = menor = None
    soma = 0.0
    quantidade = 0
    numero = float(input("Digite um número (-1 para encerrar): "))
    while numero != -1:
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero
        soma += numero
        quantidade += 1
        numero = float(input("Digite um número (-1 para encerrar): "))

    if quantidade == 0:
        print("Nenhum número foi digitado.")
    else:
        print(f"Maior: {maior} | Menor: {menor} | Média: {soma / quantidade:.2f}")


def ex13() -> None:
    """Tabuada de 3 a 6."""
    tabuada = 3
    while tabuada <= 6:
        print(f"\nTabuada do {tabuada}")
        i = 1
        while i <= 10:
            print(f"{tabuada} x {i} = {tabuada * i}")
            i += 1
        tabuada += 1


def ex14() -> None:
    """Fatorial de 5."""
    n = 5
    fatorial = 1
    contador = n
    while contador > 1:
        fatorial *= contador
        contador -= 1
    print(f"{n}! = {fatorial}")


def ex15() -> None:
    """Série de Fibonacci até o 15º termo."""
    anterior, atual = 1, 1
    termo = 1
    while termo <= 15:
        print(anterior, end=" ")
        anterior, atual = atual, anterior + atual
        termo += 1
    print()


EXERCICIOS = {
    1: ex01, 2: ex02, 3: ex03, 4: ex04, 5: ex05, 6: ex06, 7: ex07, 8: ex08,
    9: ex09, 10: ex10, 11: ex11, 12: ex12, 13: ex13, 14: ex14, 15: ex15,
}  # fmt: skip


def main() -> None:
    numero = int(input(f"Qual exercício executar (1-{len(EXERCICIOS)})? "))
    EXERCICIOS[numero]()


if __name__ == "__main__":
    main()
