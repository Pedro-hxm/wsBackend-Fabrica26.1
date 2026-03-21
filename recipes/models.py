from django.db import models
from django.contrib.auth.models import User

# Ingredientes
class ingradiente(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
#receita 
class Recipe(models.Model):

    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    imagens = models.URLField()
    instrucoes = models.TextField()

    ingradientes = models.ManyToManyField(ingradiente, through='ReceitaIngrediente')

    def __str__(self):
        return self.nome

# tabela de associação entre receita e ingrediente
class ReceitaIngrediente(models.Model):

    receita = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingradiente = models.ForeignKey(ingradiente, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=100)
    unidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantidade} {self.unidade} de {self.ingradiente.nome} para {self.receita.nome}"

class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receita = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} favoritou {self.receita.nome}"

# Create your models here.
