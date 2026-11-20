from decimal import Decimal

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_produtos(request: HttpRequest) -> HttpResponse:
    """Aula 24: renderiza um template usando um contexto.

    O dicionário `context` SIMULA dados vindos de um banco de dados. Na aula 25 os dados passam a vir
    de um Model; aqui a camada Template já mostra como exibi-los com a Django Template Language.
    """
    context = {
        # Exemplo 1: um único produto
        "produto": "Tablet iPad",
        "preco": Decimal("4550.00"),
        # Exemplo 2: vários produtos
        "produtos": [
            {"produto": "Smart TV LG 70 Polegadas", "preco": Decimal("5250.00")},
            {"produto": "Smart TV Samsung 50 Polegadas", "preco": Decimal("3000.00")},
            {"produto": "Smart TV Philips 42 Polegadas", "preco": Decimal("2100.00")},
        ],
    }
    return render(request, "produtos/index.html", context)


def celulares(request: HttpRequest) -> HttpResponse:
    """Aula 21: a resposta mais simples possível, um texto puro sem template."""
    return HttpResponse("Página de celulares")
