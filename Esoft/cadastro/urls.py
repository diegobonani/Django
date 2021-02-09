from django.urls import path
from . import views
from .views import update_pessoas, deletar_pessoas

urlpatterns = [
    path('cadastro/', views.paginaInicial, name='paginaInicial'),
    path('pessoas/', views.pessoasCadastradas, name='pessoasCadastradas'),
    path('atualizacao/<int:id>/', views.update_pessoas, name='update_pessoa'),
    path('deletar/<int:id>/', views.deletar_pessoas, name='deletar_pessoa'),
]