"""Associação: um objeto usa outro, sem que um dependa do outro."""

from __future__ import annotations


class Academia:
    def __init__(self, nome_academia: str, atividade: str) -> None:
        self.nome_academia = nome_academia
        self.atividade = atividade

    def praticar_atividade(self) -> str:
        return f"está fazendo {self.atividade} na academia {self.nome_academia}"


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.exercicio: Academia | None = None  # associação: guarda uma Academia (ou nada)

    def estudar(self) -> None:
        print(f"{self.nome} está estudando Python")


if __name__ == "__main__":
    pessoa1 = Pessoa("Rafael")
    pessoa2 = Pessoa("Juliana")

    academia1 = Academia("Fit Total", "Musculação")
    academia2 = Academia("Gym Fight", "Judô")

    # As academias existem independentemente das pessoas.
    pessoa1.exercicio = academia1
    pessoa2.exercicio = academia2

    # Pelo atributo exercicio é possível acionar um método de Academia.
    for pessoa in (pessoa1, pessoa2):
        if pessoa.exercicio:
            print(f"{pessoa.nome} {pessoa.exercicio.praticar_atividade()}")

    pessoa3 = Pessoa("Marcos")  # sem academia associada
    print(f"Marcos tem academia? {pessoa3.exercicio is not None}")
