from django.db import models

class Grupos(models.Model):
    grupo = models.CharField('Grupo', max_length=200)
    projeto= models.CharField('Nome do Projeto', max_length=200)
    cliente = models.CharField('Nome do Cliente', max_length=200)
    n_de_part = models.DecimalField('Número de Participantes', max_digits=100, decimal_places=0)
    descricao = models.CharField('Descrição do Projeto', max_length=200)
    ver = models.CharField('Link de Visualização', max_length=200)
    status = models.CharField('Progresso', max_length=200)
    dataIni = models.DateField('Data de Inicio')
    dataFim = models.DateField('Data Prevista Para o Termíno')
    tutorial = models.CharField('tutorial', max_length=200)
    
    def __str__(self):
        return self.grupo