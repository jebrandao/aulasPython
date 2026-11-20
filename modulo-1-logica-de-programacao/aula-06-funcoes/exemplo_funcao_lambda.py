"""Funções lambda: funções anônimas de uma única expressão."""


def somar(n1: float, n2: float) -> float:
    return n1 + n2


# Equivalente em lambda. Por convenção (PEP 8), prefira def quando for dar nome à função;
# a lambda brilha quando usada na hora, como argumento de outra função:
soma = lambda n1, n2: n1 + n2  # noqa: E731

if __name__ == "__main__":
    print(somar(2, 3))  # 5
    print(soma(3, 4))  # 7

    alunos = [("Rafael", 9.0), ("Aline", 6.0), ("Carla", 9.5)]
    por_nota = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
    print(por_nota)

    aprovados = list(filter(lambda aluno: aluno[1] >= 7, alunos))
    print(aprovados)
