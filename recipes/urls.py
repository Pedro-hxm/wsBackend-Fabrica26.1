from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:receita_id>/', views.favoritar_receita, name='favoritar_receita'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('salvar-api/<str:meal_id>/', views.salvar_receita_api, name='salvar_receita_api'),

    path('receitas/criar/', views.criar_receita, name='criar_receita'),
    path('receitas/gerenciar/', views.gerenciar_receitas, name='gerenciar_receitas'),
    path('receitas/<int:receita_id>/editar/', views.editar_receita, name='editar_receita'),
    path('receitas/<int:receita_id>/excluir/', views.excluir_receita, name='excluir_receita'),
]