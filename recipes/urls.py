from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:receita_id>/', views.favoritar_receita, name='favoritar_receita'),
]