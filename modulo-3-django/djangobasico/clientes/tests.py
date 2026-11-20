from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class ClienteModelTests(TestCase):
    def test_str_devolve_o_nome(self) -> None:
        cliente = Cliente(
            nome="Rafaela de Alencar", email="rafaela@email.com", nascimento=date(2001, 11, 27)
        )
        self.assertEqual(str(cliente), "Rafaela de Alencar")

    def test_save_e_consulta(self) -> None:
        """Repete o que a aula 27 faz no shell."""
        cliente = Cliente(nome="Rafaela", email="rafaela@email.com", nascimento="2001-11-27")
        cliente.save()
        self.assertIsNotNone(cliente.pk)
        cliente.nascimento = "2000-01-01"
        cliente.save()
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.filter(id=cliente.id).count(), 1)


class ClienteViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.rafaela = Cliente.objects.create(
            nome="Rafaela", email="rafaela@email.com", nascimento=date(2001, 11, 27)
        )
        cls.carlos = Cliente.objects.create(
            nome="Carlos", email="carlos@email.com", nascimento=date(1995, 3, 14)
        )

    def test_lista_mostra_clientes_do_banco(self) -> None:
        resposta = self.client.get(reverse("clientes:index_clientes"))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "clientes/index.html")
        self.assertContains(resposta, "Rafaela")
        self.assertContains(resposta, "Carlos")
        self.assertContains(resposta, "Total de clientes: 2")
        self.assertContains(resposta, "27/11/2001")

    def test_lista_vazia(self) -> None:
        Cliente.objects.all().delete()
        resposta = self.client.get(reverse("clientes:index_clientes"))
        self.assertContains(resposta, "Nenhum cliente cadastrado.")

    def test_pagina_do_cliente(self) -> None:
        resposta = self.client.get(reverse("clientes:cliente_id", args=[self.rafaela.id]))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "clientes/item_cliente.html")
        self.assertContains(resposta, "rafaela@email.com")

    def test_cliente_inexistente_gera_404(self) -> None:
        resposta = self.client.get(reverse("clientes:cliente_id", args=[9999]))
        self.assertEqual(resposta.status_code, 404)

    def test_arquivos_estaticos_sao_referenciados(self) -> None:
        resposta = self.client.get("/clientes/")
        self.assertContains(resposta, "/static/css/estilos_clientes.css")
        self.assertContains(resposta, "/static/js/script_clientes.js")
        self.assertContains(resposta, "/static/images/pessoas.svg")
