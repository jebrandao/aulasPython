"""Lançando exceções: a função não trata o erro, apenas o repassa para quem a chamou (raise)."""


def dividir(n1: float, n2: float) -> None:
    try:
        print(f"{n1} / {n2} = {n1 / n2}")
    except ZeroDivisionError:
        print("(dividir) Percebi o erro, mas quem decide o que fazer é quem me chamou.")
        raise  # relança a MESMA exceção


if __name__ == "__main__":
    try:
        dividir(10, 0)
    except Exception as erro:
        print(f"DESENVOLVEDOR: Erro encontrado -> {erro}")
