from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)  # Aula 26: registra o model na área administrativa
class ClienteAdmin(admin.ModelAdmin):
    """Personaliza a listagem: várias colunas de uma vez, busca e filtro por data."""

    list_display = ("nome", "email", "nascimento")
    search_fields = ("nome", "email")
    list_filter = ("nascimento",)
