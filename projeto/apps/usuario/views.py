from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import *


def verificacao(request):
    try:
       if request.session["id"]: 
           return True
    except:
        return False
 
def login(request):
    
    if verificacao(request):
        return HttpResponseRedirect('/')
    
    template_name = 'usuario/login.html'
    
    if request.method == "POST":
        
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        if Usuario.objects.filter(email = email).exists():
        
        
            if Usuario.objects.filter(email = email ,senha = senha).exists():
            
                usuario = Usuario.objects.get(email = email, senha = senha)
            
                request.session['email'] = usuario.email
                request.session['nome'] = usuario.nome
                request.session['id'] = usuario.id
                return HttpResponseRedirect('/')
        
    return TemplateResponse(request, template_name, locals())       

 
    
def logout(request):
    try:
        del request.session['email']
        del request.session['nome']
        del request.session['id'] 
    except KeyError:
        pass
    
    return HttpResponseRedirect('/')
 


class AlunosCad(CreateView):
    model = Aluno
    fields = ['nome','email','cpf','curso','universidade','lattes','git','observacao']
    template_name = 'usuario/cadastro_aluno.html'
    success_url = reverse_lazy('usuario:alunos_listagem')


class AlunosListagem(ListView):
    model = Aluno
    template_name = 'usuario/listar_cadastros.html'