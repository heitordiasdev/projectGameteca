from django.db import models
from django.contrib.auth.models import User
class Dev(models.Model):

    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=50)



    def __str__(self):
        return self.nome

class Plat(models.Model):
    nome = models.CharField(max_length=50)



    def __str__(self):
        return self.nome
class Game(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    data_lanc = models.IntegerField()
    genero = models.ManyToManyField(Genero)
    plataforma = models.ManyToManyField(Plat)
    enredo = models.TextField()
    critica = models.TextField()
    avaliacao = models.IntegerField()
    dev = models.ManyToManyField(Dev)
    publicado = models.BooleanField(default=False)
    capa_game = models.ImageField(upload_to='capas/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome
