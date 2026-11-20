"""Extra moderno: o mesmo exemplo de herança usando @dataclass."""

from dataclasses import dataclass


@dataclass
class Pessoa:
    matricula: int
    nome: str
    email: str


@dataclass
class Aluno(Pessoa):
    curso: str
    turma: str


@dataclass
class Professor(Pessoa):
    formacao: str


if __name__ == "__main__":
    alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
    prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

    print(alu1)
    print(prof1)
    print(alu1.nome, "|", prof1.formacao)
