from django.test import TestCase
from django.urls import reverse


class InicioTests(TestCase):
    def test_pagina_inicial_renderiza_template(self) -> None:
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "inicio/index.html")

    def test_pagina_inicial_tem_links_para_as_apps(self) -> None:
        resposta = self.client.get(reverse("inicio:index"))
        self.assertContains(resposta, reverse("produtos:index_produtos"))
        self.assertContains(resposta, reverse("clientes:index_clientes"))
