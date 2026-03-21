import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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



    
# Create your views here.
