import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Receita, ReceitaIngrediente, Favoritos, Ingrediente


def home(request):
    receitas = Receita.objects.all()

    dados = []
    
    for receita in receitas:
        ingredientes = ReceitaIngrediente.objects.filter(receita=receita)

        dados.append({
            'receita': receita,
            'ingredientes': ingredientes
        })

    favoritos = []

    if request.user.is_authenticated:
        favoritos = Favoritos.objects.filter(usuario=request.user)



    receitas_api = []
    busca = request.GET.get('busca')

    if busca: 
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={busca}"
        response = requests.get(url)
        resultado = response.json()

        if resultado['meals']:
            receitas_api = resultado['meals']
        
    return render(request, 'recipes/recipes.html', {
        'dados': dados,
        'favoritos': favoritos,
        'receitas_api': receitas_api,
        'busca': busca
        })



        
    usuario = User.objects.first()
    

    return render(request, 'recipes/recipes.html', {
        'dados': dados,
        'favoritos': favoritos})



def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'recipes/cadastro.html', {
                'erro': 'Este usuário já existe.'
            })

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'recipes/cadastro.html')


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'recipes/login.html', {
                'erro': 'Usuário ou senha inválidos.'
            })

    return render(request, 'recipes/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

@login_required
def favoritar_receita(request, receita_id):

    receita = get_object_or_404(Receita, id=receita_id)

    Favoritos.objects.get_or_create(usuario=usuario, receita=receita)

    return redirect('home')

@login_required
def salvar_receita_api(request, meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url)
    resultado = response.json()

    if not resultado['meals']:
        return redirect('home')

    meal = resultado['meals'][0]

    receita, criada = Receita.objects.get_or_create(
        nome=meal['strMeal'],
        defaults={
            'categoria': meal['strCategory'] or 'Sem categoria',
            'imagens': meal['strMealThumb'] or '',
            'instrucoes': meal['strInstructions'] or ''
        }
    )

    for i in range(1, 21):
        nome_ingrediente = meal.get(f'strIngredient{i}')
        medida = meal.get(f'strMeasure{i}')

        if nome_ingrediente and nome_ingrediente.strip():
            ingrediente_obj, _ = Ingrediente.objects.get_or_create(
                nome=nome_ingrediente.strip()
            )

            quantidade = ''
            unidade = ''

            if medida and medida.strip():
                partes = medida.strip().split(' ', 1)
                quantidade = partes[0]
                if len(partes) > 1:
                    unidade = partes[1]

            ReceitaIngrediente.objects.get_or_create(
                receita=receita,
                ingrediente=ingrediente_obj,
                defaults={
                    'quantidade': quantidade or '1',
                    'unidade': unidade or 'unidade'
                }
            )

    return redirect('home')

    
# Create your views here.
