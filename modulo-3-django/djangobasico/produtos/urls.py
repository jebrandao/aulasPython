from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.index_produtos, name="index_produtos"),
    path("celulares/", views.celulares, name="celulares"),
]
