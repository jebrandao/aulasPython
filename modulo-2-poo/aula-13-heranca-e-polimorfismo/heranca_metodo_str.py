"""Herança com __str__: as subclasses reaproveitam o texto da superclasse via super().__str__()."""


class Pessoa:
    def __init__(self, matricula: int, nome: str, email: str) -> None:
        self._matricula = matricula
        self._nome = nome
        self._email = email

    @property
    def matricula(self) -> int:
        return self._matricula

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"{self._matricula}:\nNome: {self._nome}\nE-mail: {self._email}"


class Aluno(Pessoa):
    def __init__(self, matricula: int, nome: str, email: str, curso: str, turma: str) -> None:
        super().__init__(matricula, nome, email)
        self._curso = curso
        self._turma = turma

    def __str__(self) -> str:
        return (
            f"\nDADOS DO(A) ALUNO(A) {super().__str__()}"
            f"\nCurso: {self._curso}\nTurma: {self._turma}"
        )


class Professor(Pessoa):
    def __init__(self, matricula: int, nome: str, email: str, formacao: str) -> None:
        super().__init__(matricula, nome, email)
        self._formacao = formacao

    def __str__(self) -> str:
        return f"\nDADOS DO(A) PROFESSOR(A) {super().__str__()}\nFormação: {self._formacao}"


if __name__ == "__main__":
    alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
    prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

    print(alu1)
    print(prof1)
