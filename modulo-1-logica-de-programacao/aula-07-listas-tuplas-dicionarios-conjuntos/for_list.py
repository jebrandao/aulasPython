"""Laços em listas: busca de todas as posições de uma letra e uso de enumerate."""


def posicoes_da_letra(letras: list[str], pesquisa: str) -> list[int]:
    """Devolve os índices onde a letra aparece, ignorando maiúsculas/minúsculas."""
    return [i for i, letra in enumerate(letras) if letra.lower() == pesquisa.lower()]


if __name__ == "__main__":
    # A lista tem letras repetidas, maiúsculas e minúsculas.
    letras_diversas = ["R", "i", "o", "D", "e", "J", "a", "n", "e", "i", "r", "o"]
    print(letras_diversas)

    pesquisa = input("Digite uma letra para pesquisa em letras_diversas: ")
    localizacao = posicoes_da_letra(letras_diversas, pesquisa)

    # Uma lista vazia é "falsa" em Python (len(localizacao) == 0).
    if not localizacao:
        print(f"--- {pesquisa} não localizada em letras_diversas ---")
    else:
        print(f"--- {pesquisa} foi encontrada {len(localizacao)} vez(es) em letras_diversas ---")
        print(localizacao)

    print("\n--- Percorrendo diretamente os itens ---")
    mensagens = [
        "Olá Mundo!",
        "Python é melhor que Java",
        "Na verdade TUDO depende do Banco de Dados",
        "Alguém aqui falou em programação No-Code?",
    ]
    for mensagem in mensagens:
        print(mensagem)

    print("\n--- Com índice (enumerate) ---")
    for indice, mensagem in enumerate(mensagens):
        print(f"{indice} - {mensagem}")
