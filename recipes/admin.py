from django.contrib import admin
from .models import ingradiente, Recipe, ReceitaIngrediente, Favoritos

admin.site.register(ingradiente)
admin.site.register(Recipe)
admin.site.register(ReceitaIngrediente)
admin.site.register(Favoritos)

# Register your models here.
