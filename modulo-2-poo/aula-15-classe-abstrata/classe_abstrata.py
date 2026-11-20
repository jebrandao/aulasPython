"""Classe abstrata: Pessoa não pode ser instanciada; Aluno e Professor são obrigados a completá-la."""

from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, matricula: int, nome: str, email: str) -> None:
        self._matricula = matricula
        self._nome = nome
        self._email = email

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email

    # Método CONCRETO: já vem pronto para todas as subclasses.
    def exibir_matricula_nome(self) -> None:
        print(f"\nMatrícula: {self._matricula}")
        print(f"Nome: {self._nome}")

    # Método ABSTRATO: sem corpo; cada subclasse DEVE implementar.
    @abstractmethod
    def exibir_nome_email(self) -> None: ...

    # Propriedade abstrata: também pode ser exigida das subclasses.
    @property
    @abstractmethod
    def papel(self) -> str: ...


class Aluno(Pessoa):
    def __init__(self, matricula: int, nome: str, email: str, curso: str, turma: str) -> None:
        super().__init__(matricula, nome, email)
        self._curso = curso
        self._turma = turma

    @property
    def papel(self) -> str:
        return "Aluno(a)"

    def exibir_nome_email(self) -> None:
        print(f"\nALUNO(A) {self.nome} - EMAIL: {self.email}")


class Professor(Pessoa):
    def __init__(self, matricula: int, nome: str, email: str, formacao: str) -> None:
        super().__init__(matricula, nome, email)
        self._formacao = formacao

    @property
    def papel(self) -> str:
        return "Professor(a)"

    def exibir_nome_email(self) -> None:
        print(f"\nPROFESSOR(A) {self.nome} - EMAIL: {self.email}")


class Visitante(Pessoa):
    """Subclasse incompleta de propósito: não implementa os métodos abstratos."""


if __name__ == "__main__":
    alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
    prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

    alu1.exibir_matricula_nome()
    prof1.exibir_matricula_nome()
    alu1.exibir_nome_email()
    prof1.exibir_nome_email()
    print(f"\nPapéis: {alu1.papel} e {prof1.papel}")

    print("\n--- Tentando instanciar a classe abstrata ---")
    try:
        pessoa1 = Pessoa(1000, "Rogério Barros", "rogerio@email.com")  # type: ignore[abstract]
    except TypeError as erro:
        print(f"Erro esperado: {erro}")

    print("\n--- Tentando instanciar subclasse que não implementa os métodos abstratos ---")
    try:
        visitante = Visitante(2000, "Visitante", "visitante@email.com")  # type: ignore[abstract]
    except TypeError as erro:
        print(f"Erro esperado: {erro}")
