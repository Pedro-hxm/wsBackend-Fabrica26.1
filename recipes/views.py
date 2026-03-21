from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Receita, ReceitaIngrediente, Favoritos




def home(request):
    receitas = Receita.objects.all()

    dados = []
    
    for receita in receitas:
        ingredientes = ReceitaIngrediente.objects.filter(receita=receita)

        dados.append({
            'receita': receita,
            'ingredientes': ingredientes
        })

    usuario = User.objects.first()
    favoritos = Favoritos.objects.filter(usuario=usuario)

    return render(request, 'recipes/recipes.html', {
        'dados': dados,
        'favoritos': favoritos})
    

def favoritar_receita(request, receita_id):

    receita = get_object_or_404(Receita, id=receita_id)
    usuario = User.objects.first()  

    Favoritos.objects.get_or_create(usuario=usuario, receita=receita)

    return redirect('home')



    
# Create your views here.
