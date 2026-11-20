from django.urls import path

from . import views

# app_name cria um "namespace": as rotas são chamadas por "clientes:nome_da_rota".
app_name = "clientes"

urlpatterns = [
    path("", views.index_clientes, name="index_clientes"),
    # <int:id> captura um número da URL e o entrega à view como argumento `id`.
    path("<int:id>/", views.cliente_id, name="cliente_id"),
]
