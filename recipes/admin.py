from django.contrib import admin
from .models import Ingrediente, Receita, ReceitaIngrediente, Favoritos

admin.site.register(Ingrediente)
admin.site.register(Receita)
admin.site.register(ReceitaIngrediente)
admin.site.register(Favoritos)

# Register your models here.
