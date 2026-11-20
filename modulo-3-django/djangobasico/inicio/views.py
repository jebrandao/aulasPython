from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Página inicial do site (aula 23)."""
    return render(request, "inicio/index.html")
