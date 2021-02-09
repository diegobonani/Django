from django.db import models

class CadastroPessoas(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_nascimento = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    email = models.EmailField()
    apelido = models.CharField(max_length=40, unique=True, blank=True, null=True)
    observacao = models.TextField(blank=True)