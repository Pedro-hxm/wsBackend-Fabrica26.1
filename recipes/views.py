from django.shortcuts import render
from .models import Recipe, ingradiente, ReceitaIngrediente, Favoritos


def home(request):
    receitas = Recipe.objects.all()

    dados = []
    
    for receita in Recipe.objects.all():
        ingradientes = ReceitaIngrediente.objects.filter(receita=receita)

        dados.append({
            'receita': receita,
            'ingradientes': ingradientes
        })


    return render(request, 'recipes/recipes.html', {'dados': dados})
    
# Create your views here.
