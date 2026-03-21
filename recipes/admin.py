from django.contrib import admin
from .models import ingrediente, Receita, ReceitaIngrediente, Favoritos

admin.site.register(ingrediente)
admin.site.register(Receita)
admin.site.register(ReceitaIngrediente)
admin.site.register(Favoritos)

# Register your models here.
