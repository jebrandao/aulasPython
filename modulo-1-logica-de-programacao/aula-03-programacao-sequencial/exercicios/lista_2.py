"""Lista 2 de exercícios de programação sequencial – resolução sugerida.

Execute e escolha o número do exercício: python lista_2.py
"""


def ex01() -> None:
    """Conta do restaurante com 10% de gorjeta."""
    conta = float(input("Valor da conta (R$): "))
    print(f"Total com 10% de gorjeta: R$ {conta * 1.10:.2f}")


def ex02() -> None:
    """Minutos transcorridos desde 00:00."""
    horas = int(input("Horas atuais: "))
    minutos = int(input("Minutos atuais: "))
    print(f"Desde as 00:00h já se passaram {horas * 60 + minutos} minutos.")


def ex03() -> None:
    """Peso em gramas e altura em centímetros."""
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    print(f"Peso: {peso * 1000:.0f} g")
    print(f"Altura: {altura * 100:.0f} cm")


def ex04() -> None:
    """IMC = peso / altura²."""
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    print(f"Seu IMC é {peso / altura**2:.2f}")


def ex05() -> None:
    """Seis operações entre dois números."""
    a = float(input("1º número: "))
    b = float(input("2º número: "))
    print(f"Soma: {a + b}")
    print(f"Primeiro - segundo: {a - b}")
    print(f"Segundo - primeiro: {b - a}")
    print(f"Multiplicação: {a * b}")
    print(f"Primeiro / segundo: {a / b}")
    print(f"Resto de primeiro / segundo: {a % b}")


def ex06() -> None:
    """Salário de vendedor: fixo + 15% de comissão sobre as vendas."""
    nome = input("Nome do vendedor: ")
    fixo = float(input("Salário fixo (R$): "))
    vendas = float(input("Total de vendas no mês (R$): "))
    comissao = vendas * 0.15
    print(f"\nVendedor: {nome}")
    print(f"Salário fixo: R$ {fixo:.2f}")
    print(f"Comissão (15%): R$ {comissao:.2f}")
    print(f"Salário final: R$ {fixo + comissao:.2f}")


def ex07() -> None:
    """Valor das prestações (até 10x sem juros)."""
    compra = float(input("Valor da compra (R$): "))
    parcelas = int(input("Número de prestações (1 a 10): "))
    print(f"{parcelas}x de R$ {compra / parcelas:.2f} sem juros")


def ex08() -> None:
    """Preço de venda a partir do custo e de um percentual de acréscimo."""
    custo = float(input("Preço de custo (R$): "))
    percentual = float(input("Percentual de acréscimo (%): "))
    print(f"Preço de venda: R$ {custo * (1 + percentual / 100):.2f}")


def ex09() -> None:
    """Idade em anos, meses e dias convertida para dias (ano = 365, mês = 30)."""
    anos = int(input("Anos: "))
    meses = int(input("Meses: "))
    dias = int(input("Dias: "))
    print(f"Idade total: {anos * 365 + meses * 30 + dias} dias")


def ex10() -> None:
    """Percentual de votos brancos, nulos e válidos."""
    total = int(input("Total de eleitores: "))
    brancos = int(input("Votos em branco: "))
    nulos = int(input("Votos nulos: "))
    validos = int(input("Votos válidos: "))
    print(f"Brancos: {brancos / total:.2%}")
    print(f"Nulos: {nulos / total:.2%}")
    print(f"Válidos: {validos / total:.2%}")


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
