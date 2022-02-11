from django.db import models

class Grupos(models.Model):
    grupo = models.CharField('Nome do Grupo', max_length=200)
    projeto= models.CharField('Nome do Projeto', max_length=200)
    cliente = models.CharField('Nome do Cliente', max_length=200)
    n_de_part = models.DecimalField(max_digits=100, decimal_places=10)
    descricao = models.CharField('Descrição do Projeto', max_length=200)
    tutorial = models.CharField('tutorial', max_length=200)
    ver = models.CharField('ver', max_length=200)
    
    
    def __str__(self):
        return self.grupo
# Create your models here.
# Create your models here.
