"""Rotas do projeto (aulas 21, 22 e 23).

O urls.py do PROJETO define o início de cada rota e delega o restante para o urls.py de cada app
com include(). A rota vazia ("") aponta para a app `inicio`, que serve a página inicial.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # Aula 26: área administrativa
    path("", include("inicio.urls")),  # Aula 23: página inicial
    path("produtos/", include("produtos.urls")),  # Aulas 21 e 24
    path("clientes/", include("clientes.urls")),  # Aulas 22 e 25 a 29
]
