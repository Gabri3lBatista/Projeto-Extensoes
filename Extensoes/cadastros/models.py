from django.db import models

class Grupos(models.Model):
    grupo = models.CharField('Digite o nome do grupo', max_length=200)
    projeto= models.CharField('Digite o nome do projeto', max_length=200)
    cliente = models.CharField('Digite o nome do cliente', max_length=200)
    n_de_part = models.DecimalField(max_digits=100, decimal_places=10)
    descricao = models.CharField('Descrição do projeto', max_length=200)
    tutorial = models.CharField('tutorial', max_length=200)
    ver = models.CharField('ver', max_length=200)
    status = models.CharField('status', max_length=200)
    dataIni = models.DateField(blank=True)
    dataFim = models.DateField(blank=True)
    
    def __str__(self):
        return self.grupo
# Create your models here.
# Create your models here.


