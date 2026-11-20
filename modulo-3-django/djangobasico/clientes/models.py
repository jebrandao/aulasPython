from django.db import models


class Cliente(models.Model):
    """Aula 25: cada classe vira uma tabela no banco e cada atributo vira uma coluna.

    O Django cria sozinho a chave primária (id) e gera o SQL: não é preciso escrever comandos SQL.
    """

    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("e-mail", max_length=100)
    nascimento = models.DateField("data de nascimento")

    class Meta:
        ordering = ["nome"]

    def __str__(self) -> str:
        """Aula 26: sem este método a lista do admin mostra "Cliente object (1)" para todos."""
        return self.nome
