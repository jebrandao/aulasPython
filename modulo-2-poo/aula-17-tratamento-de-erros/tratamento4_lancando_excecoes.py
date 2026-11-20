"""Lançando exceções: valida a condição antes e levanta uma exceção com mensagem clara."""


def dividir(n1: float, n2: float) -> float:
    if n2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    return n1 / n2


if __name__ == "__main__":
    try:
        print(dividir(10, 2))
        print(dividir(10, 0))
    except ValueError as erro:
        print(f"DESENVOLVEDOR: Erro encontrado -> {erro}")

    # raise ... from: converte o erro mantendo a causa original no traceback.
    try:
        try:
            int("abc")
        except ValueError as erro:
            raise RuntimeError("Falha ao ler a idade informada.") from erro
    except RuntimeError as erro:
        print(f"{erro} (causa: {erro.__cause__})")
