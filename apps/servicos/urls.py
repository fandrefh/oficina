from django.urls import path

app_name = 'servicos'

from . import views

urlpatterns = [
    path('novo/', views.novo_servico, name='novo_servico'),
    path('atualizar/<int:pk>/', views.atualizar_servico, name='atualizar_servico'),
    path('ordens-servicos/', views.lista_ordem_servico, name='lista_ordem_servico'),
    path('criar-ordem-servico/', views.criar_ordem_servico, name='criar_ordem_servico'),
    path('editar-ordem-servico/<int:pk>/', views.editar_ordem_servico, name='editar_ordem_servico'),
    path('', views.lista_servicos, name='lista_servicos'),
]
