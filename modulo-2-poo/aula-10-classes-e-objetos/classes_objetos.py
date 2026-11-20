"""Classe Carro e dois objetos (instâncias)."""


class Carro:
    def __init__(self, fabricante: str, modelo: str, cor: str, ano: int) -> None:
        # __init__ é o método construtor: roda ao criar cada objeto.
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


if __name__ == "__main__":
    carro1 = Carro("Fiat", "Mobi", "Preto", 2022)
    carro2 = Carro("Volkswagen", "Up", "Branco", 2020)

    for carro in (carro1, carro2):
        print(f"\nFabricante: {carro.fabricante}")
        print(f"Modelo: {carro.modelo}")
        print(f"Cor: {carro.cor}")
        print(f"Ano: {carro.ano}")

    # Cada objeto mantém seus próprios valores:
    carro1.cor = "Vermelho"
    print(f"\ncarro1 agora é {carro1.cor}; carro2 continua {carro2.cor}")
