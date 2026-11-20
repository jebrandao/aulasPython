"""Lista 2 de exercícios de decisão e operadores ternários – resolução sugerida.

Execute e escolha o número do exercício: python lista_2.py
"""


def ex01() -> None:
    """Acima ou abaixo de 1000."""
    numero = float(input("Informe um número: "))
    if numero > 1000:
        print("Acima de 1000")
    elif numero < 1000:
        print("Abaixo de 1000")
    else:
        print("Exatamente 1000")


def ex02() -> None:
    """Abaixo de 1000, entre 1000 e 5000 ou acima de 5000."""
    numero = float(input("Informe um número: "))
    if numero < 1000:
        print("Abaixo de 1000")
    elif numero <= 5000:
        print("Entre 1000 e 5000")
    else:
        print("Acima de 5000")


def ex03() -> None:
    """Abaixo de 1000, 1000-5000, 5001-8000 ou acima de 8000."""
    numero = float(input("Informe um número: "))
    if numero < 1000:
        print("Abaixo de 1000")
    elif numero <= 5000:
        print("Entre 1000 e 5000")
    elif numero <= 8000:
        print("Entre 5001 e 8000")
    else:
        print("Acima de 8000")


def ex04() -> None:
    """Dia da semana por extenso (1 = domingo)."""
    numero = int(input("Informe um número de 1 a 7: "))
    match numero:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Número inválido")


def ex05() -> None:
    """A UF informada é da região Sudeste?"""
    uf = input("Sigla do estado (UF): ").strip().upper()
    regiao_sudeste = {"SP", "RJ", "MG", "ES"}
    print(f"{uf} {'está' if uf in regiao_sudeste else 'NÃO está'} na região Sudeste.")


def ex06() -> None:
    """Idade a partir do ano de nascimento e do ano atual."""
    nascimento = int(input("Ano de nascimento: "))
    atual = int(input("Ano atual: "))
    if nascimento > atual:
        print("Dados inseridos estão incorretos")
    else:
        print(f"Idade: {atual - nascimento} anos")


def ex07() -> None:
    """Maior, menor ou iguais entre 2 números."""
    a = float(input("1º número: "))
    b = float(input("2º número: "))
    if a == b:
        print("Os números são iguais.")
    else:
        print(f"Maior: {max(a, b)} | Menor: {min(a, b)}")


def ex08() -> None:
    """Maior de 3 números."""
    a = float(input("1º número: "))
    b = float(input("2º número: "))
    c = float(input("3º número: "))
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    print(f"Maior: {maior}")


def ex09() -> None:
    """Menor de idade, maior de idade ou maior de 65 anos."""
    idade = int(input("Informe a idade: "))
    if idade < 18:
        print("Menor de idade")
    elif idade <= 65:
        print("Maior de idade")
    else:
        print("Maior de 65 anos")


def ex10() -> None:
    """Média de duas provas: <3 reprovado, 3 a 6,9 prova final, >=7 aprovado."""
    nome = input("Nome do aluno: ")
    p1 = float(input("Nota da prova 1: "))
    p2 = float(input("Nota da prova 2: "))
    media = (p1 + p2) / 2
    if media < 3:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Prova final"
    else:
        situacao = "Aprovado"
    print(f"{nome}: média {media:.1f} - {situacao}")


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
