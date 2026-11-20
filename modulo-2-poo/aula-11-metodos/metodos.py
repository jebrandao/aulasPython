"""Métodos: a classe Usuario sabe efetuar login."""

from hmac import compare_digest

# Credenciais fixas apenas para fins didáticos.
EMAIL_CADASTRADO = "user@email.com"
SENHA_CADASTRADA = "senha123"


class Usuario:
    def __init__(self, email: str, senha: str) -> None:
        self.email = email
        self.senha = senha

    def efetuar_login(self) -> bool:
        """Devolve True se e-mail e senha conferem com o cadastro."""
        return compare_digest(self.email, EMAIL_CADASTRADO) and compare_digest(
            self.senha, SENHA_CADASTRADA
        )


if __name__ == "__main__":
    user1 = Usuario("user@email.com", "senha123")
    user2 = Usuario("rivonelson@email.com", "carro")

    for usuario in (user1, user2):
        if usuario.efetuar_login():
            print(f"e-mail: {usuario.email} --> Usuário logado com sucesso!")
        else:
            print(f"e-mail: {usuario.email} --> Não foi possível efetuar login.")
