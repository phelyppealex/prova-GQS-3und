"""
URL configuration for mel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Producao import views

app_name = 'Producao'

urlpatterns = [
    path('', views.home, name='inicio'),

    path('criar-coleta/', views.criar_coleta, name='criar_coleta'),
    path('criar-coleta-cbv/', views.CriarColeta.as_view(), name='criar_coleta_cbv'),

    path('listar-coletas/', views.listar_coletas, name='listar_coletas'),
    path('listar-coletas-cbv/', views.ListarColetas.as_view(), name='listar_coletas_cbv'),

    path('detalhes-coleta/<int:pk>', views.detalhar_coleta, name='detalhes_coleta'),
    path('listar-coletas/detalhes/<int:pk>', views.DetalharColeta.as_view(), name='detalhes_coleta_cbv'),

    path('deletar-coleta/<int:pk>', views.deletar_coleta, name='deletar_coleta'),
    path('listar-coletas/deletar-cbv/<int:pk>', views.DeletarColeta.as_view(), name='deletar_coleta_cbv'),

    path('criar-criacao/', views.criar_criacao, name='criar_criacao'),
    path('criar-criacao-cbv/', views.CriarCriacao.as_view(), name='criar_criacao_cbv'),

    path('listar-criacoes/', views.listar_criacoes, name='listar_criacoes'),
    path('listar-criacoes-cbv/', views.ListarCriacoes.as_view(), name='listar_criacoes_cbv'),

    path('detalhes-criacao/<int:pk>', views.detalhar_criacao, name='detalhes_criacao'),
    path('listar-criacoes/detalhes-cbv/<int:pk>', views.DetalharCriacao.as_view(), name='detalhes_criacao-cbv'),

    path('deletar-criacao/<int:pk>', views.deletar_criacao, name='deletar_criacao'),
    path('listar-criacoes/deletar/<int:pk>', views.DeletarCriacao.as_view(), name='detalhes_criacao_cbv'),

    path('editar-criacao/<int:pk>', views.editar_criacao, name='editar_criacao'),
    path('editar-coleta/<int:pk>', views.editar_coleta, name='editar_coleta'),
]