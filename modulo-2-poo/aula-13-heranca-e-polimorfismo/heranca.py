"""Herança: Aluno e Professor reaproveitam o que é comum em Pessoa."""


class Pessoa:
    """Superclasse (classe mãe) com as características comuns."""

    def __init__(self, matricula: int, nome: str, email: str) -> None:
        self._matricula = matricula
        self._nome = nome
        self._email = email

    @property
    def matricula(self) -> int:
        return self._matricula

    @matricula.setter
    def matricula(self, matricula: int) -> None:
        self._matricula = matricula

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email


class Aluno(Pessoa):
    """Subclasse (classe filha): declara a herança entre parênteses."""

    def __init__(self, matricula: int, nome: str, email: str, curso: str, turma: str) -> None:
        super().__init__(matricula, nome, email)  # dados que pertencem à superclasse
        self._curso = curso  # dados específicos de Aluno
        self._turma = turma

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, curso: str) -> None:
        self._curso = curso

    @property
    def turma(self) -> str:
        return self._turma

    @turma.setter
    def turma(self, turma: str) -> None:
        self._turma = turma


class Professor(Pessoa):
    def __init__(self, matricula: int, nome: str, email: str, formacao: str) -> None:
        super().__init__(matricula, nome, email)
        self._formacao = formacao

    @property
    def formacao(self) -> str:
        return self._formacao

    @formacao.setter
    def formacao(self, formacao: str) -> None:
        self._formacao = formacao


if __name__ == "__main__":
    alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
    prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

    print(f"\nDADOS DO(A) ALUNO(A) {alu1.matricula}:")
    print(f"Nome: {alu1.nome}")  # atributo da superclasse Pessoa
    print(f"E-mail: {alu1.email}")  # atributo da superclasse Pessoa
    print(f"Curso: {alu1.curso}")  # atributo da subclasse Aluno
    print(f"Turma: {alu1.turma}")

    print(f"\nDADOS DO(A) PROFESSOR(A) {prof1.matricula}:")
    print(f"Nome: {prof1.nome}")
    print(f"E-mail: {prof1.email}")
    print(f"Formação: {prof1.formacao}")

    print(f"\nAluno é uma Pessoa? {isinstance(alu1, Pessoa)}")
    print(f"Hierarquia de Aluno: {[c.__name__ for c in Aluno.__mro__]}")
