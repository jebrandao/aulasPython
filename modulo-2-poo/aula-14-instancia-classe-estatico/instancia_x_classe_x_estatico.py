"""Cooperativa Táxi Rio: atributos e métodos de instância, de classe e estáticos."""


class TaxiRio:
    # Atributo de CLASSE: compartilhado por todos os táxis (na capital, todos são amarelos).
    cor = "Amarelo"

    def __init__(self, fabricante: str, modelo: str, ano: int) -> None:
        # Atributos de INSTÂNCIA: cada táxi tem os seus.
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano

    @property
    def fabricante(self) -> str:
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante: str) -> None:
        self._fabricante = fabricante

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self._modelo = modelo

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, ano: int) -> None:  # no slide estava (errado) "def fabricante"
        self._ano = ano

    def __str__(self) -> str:
        return (
            "Características do Taxi Selecionado:\n"
            f"-- Fabricante: {self._fabricante}\n"
            f"-- Modelo: {self._modelo}\n"
            f"-- Ano: {self._ano}\n"
            f"-- Cor: {self.cor}\n"
        )

    # Método de INSTÂNCIA: precisa de self (usa dados deste táxi).
    def exibir_fabricante_modelo(self) -> None:
        print(f"Você está aguardando um Táxi {self._fabricante} {self._modelo}.")

    # Método de CLASSE: recebe cls (usa dados da classe, não de um táxi específico).
    @classmethod
    def exibir_cor(cls) -> None:
        print(f"A cor padrão dos táxis na capital do Rio de Janeiro é {cls.cor}.")

    # Método ESTÁTICO: não recebe self nem cls; poderia ser uma função comum.
    @staticmethod
    def exibir_horario_de_funcionamento() -> None:
        print("A Táxi Rio está à sua disposição 24h por dia.")


if __name__ == "__main__":
    taxi1 = TaxiRio("Toyota", "Corolla", 2023)
    taxi2 = TaxiRio("Honda", "Civic", 2022)
    taxi3 = TaxiRio("Chevrolet", "Cruze", 2021)

    for taxi in (taxi1, taxi2, taxi3):
        print(taxi)

    print("--- Métodos de instância (dependem do objeto) ---")
    for taxi in (taxi1, taxi2, taxi3):
        taxi.exibir_fabricante_modelo()

    print("\n--- Método de classe (por instância ou direto pela classe) ---")
    taxi1.exibir_cor()
    TaxiRio.exibir_cor()

    print("\n--- Método estático ---")
    TaxiRio.exibir_horario_de_funcionamento()
    taxi1.exibir_horario_de_funcionamento()

    print("\n--- Cuidado ao alterar atributo de classe ---")
    taxi1.cor = "Azul"  # cria atributo de INSTÂNCIA só em taxi1; o da classe não muda
    print(f"taxi1.cor = {taxi1.cor} | taxi2.cor = {taxi2.cor} | TaxiRio.cor = {TaxiRio.cor}")
    TaxiRio.cor = "Verde"  # altera a classe: afeta quem não tem atributo próprio
    print(f"taxi1.cor = {taxi1.cor} | taxi2.cor = {taxi2.cor} | TaxiRio.cor = {TaxiRio.cor}")
