import imp
from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'usuario'

urlpatterns = [
    path('', login, name='login'),
    path('logout', logout, name='logout'),
    path('Cadastrar_Aluno', AlunosCad.as_view(), name='Cadastrar_Aluno'),
    path('alunos_listagem/', AlunosListagem.as_view(), name='alunos_listagem'),

]
