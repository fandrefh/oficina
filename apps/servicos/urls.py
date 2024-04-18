from django.urls import path

app_name = 'servicos'

from . import views

urlpatterns = [
    path('novo/', views.novo_servico, name='novo_servico'),
    path('atualizar/<int:pk>/', views.atualizar_servico, name='atualizar_servico'),
    path('', views.lista_servicos, name='lista_servicos'),
]
