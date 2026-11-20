"""Lista de exercícios de laços – somente FOR – resolução sugerida.

Execute e escolha o número do exercício: python lista_for.py
"""


def ex01() -> None:
    """Ímpares de 1000 a 1500."""
    for n in range(1001, 1501, 2):
        print(n, end=" ")
    print()


def ex02() -> None:
    """Soma de 1 até n."""
    n = int(input("Informe n: "))
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print(f"Soma de 1 até {n}: {soma}")


def ex03() -> None:
    """Tabuada de um número."""
    numero = int(input("Tabuada de qual número? "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def ex04() -> None:
    """Divisíveis por 5 menores que 50."""
    for n in range(5, 50, 5):
        print(n, end=" ")
    print()


def ex05() -> None:
    """Potências de 2 de 0 a 10."""
    for e in range(0, 11):
        print(f"2 elevado à {e} = {2**e}")


def ex06() -> None:
    """Potência b^e sem math.pow e sem **."""
    b = float(input("Base: "))
    e = int(input("Expoente (inteiro >= 0): "))
    resultado = 1.0
    for _ in range(e):  # "_" indica que a variável do laço não será usada
        resultado *= b
    print(f"{b} elevado a {e} = {resultado}")


def ex07() -> None:
    """Soma dos pares de 3 até 21."""
    soma = 0
    for n in range(4, 22, 2):
        soma += n
    print(f"Soma dos pares de 3 até 21: {soma}")


def ex08() -> None:
    """20 pessoas: exibe o nome dos homens com 21 anos ou mais."""
    selecionados = []
    for i in range(1, 21):
        print(f"\nPessoa {i} de 20")
        nome = input("Nome completo: ")
        sexo = input("Sexo (M/F): ").strip().upper()
        idade = int(input("Idade: "))
        if sexo == "M" and idade >= 21:
            selecionados.append(nome)

    print("\nHomens com 21 anos ou mais:")
    for nome in selecionados:
        print(f" - {nome}")


def ex09() -> None:
    """Múltiplos de 3 e 5 ao mesmo tempo de 1 até n."""
    n = int(input("Informe n: "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
    print()


def ex10() -> None:
    """Fatorial de um número."""
    n = int(input("Fatorial de qual número? "))
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    print(f"{n}! = {fatorial}")


def ex11() -> None:
    """Matriz de ordem 10 (completa) e apenas acima da diagonal principal."""
    print("\n       Triangulação de matriz de ordem 10")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}-{j}", end="\t")
        print()

    print("\n     Triangulação de matriz de ordem 10, acima da diagonal principal.")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}-{j}" if j > i else "x-x", end="\t")
        print()


def ex12() -> None:
    """Tabela de polegadas para centímetros (1 pol = 2,54 cm)."""
    limite = int(input("Converter de 1 polegada até quantas? "))
    print(f"{'Polegadas':>10} | {'Centímetros':>12}")
    for pol in range(1, limite + 1):
        print(f"{pol:>10} | {pol * 2.54:>12.2f}")


def ex13() -> None:
    """15 alunos: nome, nota1, nota2, média, situação e média da turma."""
    alunos = []
    for i in range(1, 16):
        nome = input(f"\nAluno {i} de 15 - Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        alunos.append((nome, nota1, nota2, (nota1 + nota2) / 2))

    print(f"\n{'Nome':<20}{'Nota 1':>8}{'Nota 2':>8}{'Média':>8}  Situação")
    soma_medias = 0.0
    for nome, nota1, nota2, media in alunos:
        situacao = "APROVADO" if media >= 5 else "REPROVADO"
        print(f"{nome:<20}{nota1:>8.1f}{nota2:>8.1f}{media:>8.1f}  {situacao}")
        soma_medias += media
    print(f"\nMédia da turma: {soma_medias / len(alunos):.2f}")


def ex14() -> None:
    """Imposto de renda de 10 pessoas: isento < 600; 10% até 1499,99; 15% a partir de 1500."""
    print("Cálculo do imposto de renda de 10 pessoas")
    for i in range(1, 11):
        nome = input(f"\nPessoa {i} de 10 - Nome: ")
        bruto = float(input("Salário bruto (R$): "))
        if bruto < 600:
            aliquota = 0.0
        elif bruto < 1500:
            aliquota = 0.10
        else:
            aliquota = 0.15
        imposto = bruto * aliquota
        print(
            f"{nome}: alíquota {aliquota:.0%} = R$ {imposto:.2f} | salário líquido R$ {bruto - imposto:.2f}"
        )


EXERCICIOS = {
    1: ex01, 2: ex02, 3: ex03, 4: ex04, 5: ex05, 6: ex06, 7: ex07,
    8: ex08, 9: ex09, 10: ex10, 11: ex11, 12: ex12, 13: ex13, 14: ex14,
}  # fmt: skip


def main() -> None:
    numero = int(input(f"Qual exercício executar (1-{len(EXERCICIOS)})? "))
    EXERCICIOS[numero]()


if __name__ == "__main__":
    main()
