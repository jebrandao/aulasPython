"""Extra moderno: a mesma classe Carro usando @dataclass."""

from dataclasses import dataclass


@dataclass
class Carro:
    fabricante: str
    modelo: str
    cor: str
    ano: int


if __name__ == "__main__":
    carro1 = Carro("Fiat", "Mobi", "Preto", 2022)
    carro2 = Carro("Fiat", "Mobi", "Preto", 2022)

    print(carro1)  # __repr__ pronto: Carro(fabricante='Fiat', modelo='Mobi', ...)
    print(carro1 == carro2)  # __eq__ compara os atributos: True
    print(carro1 is carro2)  # são objetos diferentes na memória: False
