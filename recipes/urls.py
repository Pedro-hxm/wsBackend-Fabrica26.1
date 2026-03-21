from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:receita_id>/', views.favoritar_receita, name='favoritar_receita'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]