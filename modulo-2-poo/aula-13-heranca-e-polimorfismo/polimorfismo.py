"""Polimorfismo: ContaEspecial sobrescreve calcular_saldo() herdado de ContaCorrente."""


class ContaCorrente:
    def __init__(self, titular: str, agencia: int, conta: int, saldo: float) -> None:
        self._titular = titular
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def titular(self) -> str:
        return self._titular

    @titular.setter
    def titular(self, titular: str) -> None:
        self._titular = titular

    @property
    def agencia(self) -> int:
        return self._agencia

    @property
    def conta(self) -> int:
        return self._conta

    @property
    def saldo(self) -> float:
        return self._saldo

    # No slide, este setter estava (errado) declarado como @titular.setter.
    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self._saldo = saldo

    def calcular_saldo(self) -> float:
        """Conta simples: o saldo disponível é o próprio saldo."""
        return self._saldo

    def __str__(self) -> str:
        conta = str(self._conta).zfill(7)  # converte para str com 7 dígitos (zeros à esquerda)
        conta_formatada = f"{conta[:6]}-{conta[6:]}"  # máscara 123456-7
        return (
            "---BANCO BIT---\n"
            f"Titular: {self._titular}\n"
            f"Agência: {self._agencia}\n"
            f"Conta: {conta_formatada}\n"
            f"Saldo: R$ {self._saldo:,.2f}\n"
        )


class ContaEspecial(ContaCorrente):
    def __init__(self, titular: str, agencia: int, conta: int, saldo: float, limite: float) -> None:
        super().__init__(titular, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, limite: float) -> None:
        self._limite = limite

    def calcular_saldo(self) -> float:
        """Polimorfismo: conta especial = saldo + limite."""
        return super().calcular_saldo() + self._limite

    def __str__(self) -> str:
        return f"{super().__str__()}Limite: R$ {self._limite:,.2f}\n"


if __name__ == "__main__":
    conta1 = ContaCorrente("Camilla Vieira", 3112, 9123456, 2500.00)
    conta2 = ContaEspecial("Luana Barbosa", 5110, 812345, 450.00, 1000.00)

    print(conta1)
    print(conta2)

    print(f"Conta 1 -> Saldo disponível: R$ {conta1.calcular_saldo():,.2f}")
    print(f"Conta 2 -> Saldo disponível: R$ {conta2.calcular_saldo():,.2f}")

    # O mesmo código funciona para qualquer tipo de conta; cada uma responde à sua maneira:
    print("\nTotal disponível no banco:", end=" ")
    contas = [conta1, conta2]
    print(f"R$ {sum(c.calcular_saldo() for c in contas):,.2f}")
