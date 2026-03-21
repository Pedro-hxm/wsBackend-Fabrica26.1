from django.shortcuts import render

def home(request):
    return render(request, 'recipes/recipes.html')
# Create your views here.
