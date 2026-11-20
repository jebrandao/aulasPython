"""Encapsulamento pythônico com @property: parece atributo, funciona como método."""


class ContaCorrente:
    def __init__(self, titular: str, agencia: str, numero_conta: str, saldo: float) -> None:
        self._titular = titular
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    # --- Getter + setter: titular pode ser corrigido (ex.: nome completo) ---
    @property
    def titular(self) -> str:
        return self._titular

    @titular.setter
    def titular(self, titular: str) -> None:
        if not titular.strip():
            raise ValueError("O titular não pode ser vazio.")
        self._titular = titular

    # --- Somente leitura: sem setter, tentar atribuir gera AttributeError ---
    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def numero_conta(self) -> str:
        return self._numero_conta

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para esta operação.")
        self._saldo -= valor


class ContaComNameMangling:
    """Extra: __atributo sofre name mangling (vira _ContaComNameMangling__segredo)."""

    def __init__(self) -> None:
        self.__segredo = 42


if __name__ == "__main__":
    conta1 = ContaCorrente("Fabricio", "0101", "7575-5", 1000)
    print(f"Titular: {conta1.titular}, Saldo: R$ {conta1.saldo:,.2f}")

    # Sintaxe de atributo, mas é o setter que roda (e valida):
    conta1.titular = "Fabricio Curvello"
    print(f"Titular: {conta1.titular}")

    conta1.depositar(500)
    print(f"Saldo após depósito: R$ {conta1.saldo:,.2f}")

    try:
        conta1.saldo = 0  # type: ignore[misc]
    except AttributeError as erro:
        print(f"Saldo é somente leitura: {erro}")

    try:
        conta1.sacar(10_000)
    except ValueError as erro:
        print(f"Saque recusado: {erro}")

    print("\n--- name mangling ---")
    oculta = ContaComNameMangling()
    print(hasattr(oculta, "__segredo"))  # False: o nome mudou
    print(oculta._ContaComNameMangling__segredo)  # 42 (ainda acessível, só mais difícil)
