from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Cliente


def index_clientes(request: HttpRequest) -> HttpResponse:
    """Aula 28: a View pede os dados ao Model e os entrega ao Template."""
    clientes = Cliente.objects.all()
    return render(request, "clientes/index.html", {"clientes": clientes})


def cliente_id(request: HttpRequest, id: int) -> HttpResponse:
    """Aula 28: página específica de um cliente (responde 404 se o id não existir)."""
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, "clientes/item_cliente.html", {"cliente": cliente})
