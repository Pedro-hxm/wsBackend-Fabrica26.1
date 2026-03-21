from django.shortcuts import render
from .models import Receita, ReceitaIngrediente


def home(request):
    receitas = Receita.objects.all()

    dados = []
    
    for receita in receitas:
        ingredientes = ReceitaIngrediente.objects.filter(receita=receita)

        dados.append({
            'receita': receita,
            'ingredientes': ingredientes
        })


    return render(request, 'recipes/recipes.html', {'dados': dados})



    
# Create your views here.
