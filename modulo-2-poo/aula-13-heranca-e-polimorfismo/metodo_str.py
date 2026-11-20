"""Método __str__: define como o objeto aparece em print()."""


class UsuarioSemStr:
    def __init__(self, nome: str, email: str) -> None:
        self._nome = nome
        self._email = email


class Usuario(UsuarioSemStr):
    def __str__(self) -> str:
        return f"DADOS DO(A) USUÁRIO(A) - Nome: {self._nome}, E-mail: {self._email}"


if __name__ == "__main__":
    print("Sem __str__ aparece só o tipo e o endereço de memória:")
    print(UsuarioSemStr("Jorge", "jorge@email.com"))

    print("\nCom __str__:")
    print(Usuario("Jorge", "jorge@email.com"))
    print(Usuario("Fátima", "fatima@email.com"))
