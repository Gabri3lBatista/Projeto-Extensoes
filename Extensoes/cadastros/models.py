from django.db import models

class Grupos(models.Model):
    grupo = models.CharField('Nome do Grupo', max_length=200)
    projeto= models.CharField('Nome do Projeto', max_length=200)
    cliente = models.CharField('Nome do Cliente', max_length=200)
    n_de_part = models.DecimalField('Número de Participantes', max_digits=100, decimal_places=0)
    descricao = models.CharField('Descrição do Projeto', max_length=200)
    tutorial = models.CharField('tutorial', max_length=200)
    ver = models.CharField('ver', max_length=200)
    status = models.CharField('status', max_length=200)
    dataIni = models.DateField('Data Inicio', blank=True)
    dataFim = models.DateField('Data Fim',blank=True)
    
    def __str__(self):
        return self.grupo
# Create your models here.
# Create your models here.


