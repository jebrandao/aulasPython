"""Composição: o Usuario CRIA seus Telefones; eles não existem fora dele."""


class Telefone:
    def __init__(self, ddd: int, numero: int, categorizacao: str) -> None:
        self.ddd = ddd
        self.numero = numero
        self.categorizacao = categorizacao

    def __str__(self) -> str:
        return f"- Telefone {self.categorizacao}: ({self.ddd}) {self.numero}"

    def __del__(self) -> None:
        print(f"Telefone {self.categorizacao} removido!")


class Usuario:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.telefones: list[Telefone] = []

    def cadastrar_telefone(self, ddd: int, numero: int, categorizacao: str) -> None:
        # Recebe dados avulsos; o objeto Telefone nasce AQUI DENTRO (composição).
        self.telefones.append(Telefone(ddd, numero, categorizacao))

    def listar_telefones(self) -> None:
        if not self.telefones:
            print(f"\nUsuário(a) {self.nome} - Não possui telefone cadastrado.")
            return
        print(f"\nUsuário(a) {self.nome} - Relação de Telefones:")
        for telefone in self.telefones:
            print(telefone)

    def __del__(self) -> None:
        print(f"Usuário(a) {self.nome} removido!")


if __name__ == "__main__":
    usuario1 = Usuario("Matheus")
    usuario1.cadastrar_telefone(21, 987654321, "celular")
    usuario1.cadastrar_telefone(21, 32324545, "comercial")
    usuario1.cadastrar_telefone(21, 35359898, "residencial")

    usuario2 = Usuario("Maria Alice")
    usuario2.cadastrar_telefone(21, 92221717, "celular")

    usuario3 = Usuario("Jéssica")

    usuario1.listar_telefones()
    usuario2.listar_telefones()
    usuario3.listar_telefones()

    print("\n--- Removendo o usuário 2: seus telefones são removidos junto ---")
    del usuario2

    print("\n--- Fim do programa: os demais objetos são removidos ---")
