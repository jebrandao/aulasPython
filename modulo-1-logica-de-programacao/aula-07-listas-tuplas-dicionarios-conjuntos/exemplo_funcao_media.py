"""Função que interage com dicionários e listas.

Temos uma lista onde cada item é um dicionário com o nome e as notas (em outra lista) de um aluno.
"""

from statistics import mean

alunos = [
    {"nome": "Rafael", "notas": [8, 9, 10]},
    {"nome": "Aline", "notas": [5, 7, 6]},
    {"nome": "Carla", "notas": [10, 9]},
    {"nome": "Marcos", "notas": [3, 4, 5, 6]},
]


def calcular_media(notas: list[float]) -> float:
    """Média aritmética: soma das notas dividida pela quantidade."""
    return sum(notas) / len(notas)


if __name__ == "__main__":
    print("Exibindo cada item da lista:")
    for aluno in alunos:
        print(aluno)

    print("\nExibindo com melhor manipulação dos dados:")
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']} - Notas: {aluno['notas']}")

    print("\nUsando a função calcular_media e formatando a saída:")
    for aluno in alunos:
        nome, notas = aluno["nome"], aluno["notas"]
        print(f"Nome: {nome} - Notas: {notas} - Média: {calcular_media(notas):.1f}")

    # A biblioteca padrão já traz uma função pronta:
    assert calcular_media([8, 9, 10]) == mean([8, 9, 10])

    melhor = max(alunos, key=lambda aluno: calcular_media(aluno["notas"]))
    print(f"\nMaior média: {melhor['nome']}")
