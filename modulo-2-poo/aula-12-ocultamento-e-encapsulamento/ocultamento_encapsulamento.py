"""Ocultamento e encapsulamento com getters/setters no estilo clássico (get_x / set_x)."""


class ContaCorrenteAberta:
    """Passo 1: tudo público. Qualquer um altera o saldo livremente."""

    def __init__(self, titular: str, agencia: str, numero_conta: str, saldo: float) -> None:
        self.titular = titular
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo


class ContaCorrente:
    """Passo 2: atributos "ocultos" (_) e acesso por métodos."""

    def __init__(self, titular: str, agencia: str, numero_conta: str, saldo: float) -> None:
        self._titular = titular
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    # Titular, agência e conta não costumam mudar: só getters (sem setters).
    def get_titular(self) -> str:
        return self._titular

    def get_agencia(self) -> str:
        return self._agencia

    def get_numero_conta(self) -> str:
        return self._numero_conta

    def get_saldo(self) -> float:
        return self._saldo

    # O saldo só muda por operações de negócio:
    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor
        print(f"Novo saldo: R$ {self._saldo:,.2f}")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            print("Não é possível sacar. Saldo indisponível para esta operação.")
            return
        self._saldo -= valor
        print(f"Novo saldo: R$ {self._saldo:,.2f}")


if __name__ == "__main__":
    print("--- Sem ocultamento ---")
    aberta = ContaCorrenteAberta("Fabricio", "0101", "7575-5", 1000)
    aberta.saldo = 0  # nada impede esta alteração
    print(f"Titular: {aberta.titular}, Saldo: R$ {aberta.saldo}")

    print("\n--- Com ocultamento e encapsulamento ---")
    conta1 = ContaCorrente("Fabricio", "0101", "7575-5", 1000)
    print(f"Titular: {conta1.get_titular()}, Saldo: R$ {conta1.get_saldo():,.2f}")

    conta1.depositar(500)
    conta1.sacar(2000)  # recusado: saldo insuficiente
    conta1.sacar(300)

    # O "_" é só convenção; o Python NÃO impede o acesso (mas é má prática):
    print(f"Acesso indevido ao atributo protegido: {conta1._saldo}")
