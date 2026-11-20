from django.test import TestCase
from django.urls import reverse


class ProdutosTests(TestCase):
    def test_index_renderiza_template_com_contexto(self) -> None:
        resposta = self.client.get(reverse("produtos:index_produtos"))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "produtos/index.html")
        self.assertContains(resposta, "Tablet iPad")
        self.assertContains(resposta, "Total de Smart TVs: 3")

    def test_preco_formatado_no_padrao_brasileiro(self) -> None:
        resposta = self.client.get("/produtos/")
        self.assertContains(resposta, "5.250,00")

    def test_celulares_devolve_texto_simples(self) -> None:
        resposta = self.client.get("/produtos/celulares/")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Página de celulares")
