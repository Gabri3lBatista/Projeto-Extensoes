from django.contrib import admin

from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'email', 'senha', 'adm', 'data_cadastro']
    search_fields =  ['nome', 'email', 'senha', 'adm', 'data_cadastro']

admin.site.register(Usuario, UsuarioAdmin)


class AlunoAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'curso', 'universidade', 'lattes', 'git']
    search_fields =  ['nome', 'curso', 'universidade', 'lattes', 'git']

admin.site.register(Aluno, AlunoAdmin)