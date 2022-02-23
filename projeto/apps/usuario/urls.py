import imp
from django.contrib import admin
from django.urls import path, include
from . import views

from .views import *

app_name = 'usuario'

urlpatterns = [
    path('', login, name='login'),
    path('logout', logout, name='logout'),
    path('Cadastrar_Aluno', AlunosCad.as_view(), name='Cadastrar_Aluno'),
    path('update/<int:pk>', AlunosUpdate.as_view() , name='update'),    
    path('dados_aluno/<int:pk>/', views.dados_aluno, name='dados_aluno'),
    path('alunos_listagem/', AlunosListagem.as_view(), name='alunos_listagem'),

]
