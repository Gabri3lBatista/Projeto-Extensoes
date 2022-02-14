from pyexpat import model
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=40)
    email = models.CharField('Email do Usuário', max_length=40)
    senha = models.CharField('Senha', max_length=15)
    adm = models.CharField('Adm', max_length=1, null=True, blank=True)

    data_cadastro = models.DateTimeField('Criado em', auto_now_add= True)
    
    def __str__(self):
        return self.nome
        

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=80)
    email = models.CharField('Email do Usuário', max_length=40)
    cpf = models.CharField('CPF', max_length=15)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    curso = models.CharField('Curso', max_length=100)
    universidade = models.CharField('Universidade', max_length= 50, null=True)
    lattes = models.CharField('Lattes', max_length= 60)
    git = models.CharField('Github', max_length= 60)
    observacao = models.CharField('Observações', max_length= 200)

    data_cadastro = models.DateTimeField('Cadastro em', auto_now_add= True, null=True)
    
    def __str__(self):
        return self.nome
