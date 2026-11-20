"""Módulo de cálculos: funções para serem importadas por outros arquivos."""


def calcular_media(n1: float, n2: float) -> float:
    return (n1 + n2) / 2


def situacao(media_final: float, nome: str) -> None:
    resultado = "Aprovado" if media_final >= 7 else "Reprovado"
    print(f"Nome: {nome} - Média Final: {media_final} - Situação: {resultado}")


# Este bloco só executa quando ESTE arquivo é rodado diretamente (python calculos.py),
# e não quando ele é importado por exemplo_calculos.py.
if __name__ == "__main__":
    print("Este é o arquivo de funções de cálculos")
