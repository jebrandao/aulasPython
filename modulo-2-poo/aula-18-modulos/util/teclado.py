"""Leitura de dados do teclado com validação."""


def ler_str(mensagem: str) -> str:
    """Pede um texto até que o usuário digite algo (espaços não contam)."""
    while True:
        resposta = input(mensagem).strip()
        if resposta:
            return resposta
        print("ERRO: Digite a sua resposta!")


def ler_int(mensagem: str) -> int:
    """Pede um número inteiro até que o valor digitado seja válido."""
    while True:
        try:
            return int(ler_str(mensagem))
        except ValueError:
            print("ERRO: Digite um número inteiro!")


def ler_float(mensagem: str) -> float:
    """Pede um número real. Aceita o padrão brasileiro (1.234,56) e o internacional (1234.56)."""
    while True:
        texto = ler_str(mensagem)
        if "," in texto:  # padrão brasileiro: ponto separa milhar e vírgula separa decimais
            texto = texto.replace(".", "").replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("ERRO: Digite um número válido!")


if __name__ == "__main__":
    print("\n--- Utilizando o Arquivo Python teclado.py ---\n")
