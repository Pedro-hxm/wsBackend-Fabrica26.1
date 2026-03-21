from django.db import models
from django.contrib.auth.models import User

# Ingredientes
class ingrediente(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
#receita 
class Receita(models.Model):

    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    imagens = models.URLField()
    instrucoes = models.TextField()

    ingradientes = models.ManyToManyField(ingrediente, through='ReceitaIngrediente')

    def __str__(self):
        return self.nome

# tabela de associação entre receita e ingrediente
class ReceitaIngrediente(models.Model):

    receita = models.ForeignKey(Receita, on_delete=models.CASCADE) 
    ingrediente = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=100)
    unidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantidade} {self.unidade} de {self.ingrediente.nome} para {self.receita.nome}"

class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} favoritou {self.receita.nome}"

# Create your models here.
