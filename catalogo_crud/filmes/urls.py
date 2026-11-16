from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_filmes, name="lista_filmes"),
    path("novo/", views.criar_filme, name="criar_filme"),
    path("<int:pk>/", views.detalhe_filme, name="detalhe_filme"),
    path("<int:pk>/editar/", views.editar_filme, name="editar_filme"),
    path("<int:pk>/excluir/", views.excluir_filme, name="excluir_filme"),
    path("sessao/nome/", views.salvar_nome, name="salvar_nome"),
    path("sessao/esquecer/", views.esquecer_nome, name="esquecer_nome"),
    path("tema/", views.alternar_tema, name="alternar_tema"),
]