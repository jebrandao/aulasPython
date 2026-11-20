"""Criando exceções próprias: basta herdar de Exception."""


class OpcaoInvalidaError(Exception):
    """Levantada quando o usuário escolhe uma opção inexistente no menu."""

    def __init__(self, opcao: str) -> None:
        super().__init__(f"Opção inválida: {opcao!r}")
        self.opcao = opcao  # atributo extra útil para quem trata o erro


def selecione_opcao(opcao: str) -> None:
    match opcao:
        case "1":
            print("1 - Cartões de Crédito")
        case "2":
            print("2 - Cartões de Débito")
        case "3":
            print("3 - PIX")
        case _:
            raise OpcaoInvalidaError(opcao)


if __name__ == "__main__":
    try:
        opcao = input("Informe o número da opção desejada: ")
        selecione_opcao(opcao)
    except OpcaoInvalidaError as erro:
        print(erro)
