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
    error_message = None
    
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        if Usuario.objects.filter(email = email).exists():
            if Usuario.objects.filter(email = email, senha = senha).exists():
            
                usuario = Usuario.objects.get(email = email, senha = senha)
            
                request.session['email'] = usuario.email
                request.session['nome'] = usuario.nome
                request.session['id'] = usuario.id

                return HttpResponseRedirect('/')
            else:
                error_message = "Senha de acesso incorreta!"
                return TemplateResponse(request, template_name, locals())
        else:
            error_message = "E-mail inválido ou não encontrado!"
            return TemplateResponse(request, template_name, locals())
    else:
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


class AlunosUpdate(UpdateView):
    model = Aluno
    fields = "__all__" 
    template_name = 'usuario/cadastro_aluno.html'
    success_url = reverse_lazy('usuario:alunos_listagem')

def dados_aluno(request, pk):
    list = Aluno.objects.filter(id=pk)
    context = {'dados_aluno':  list }
    return render(request, 'usuario/dados_aluno.html', context)

def excluir_aluno(request, id):
    try:
        noticia = Noticia.objects.get(id=id)
        noticia.delete()
        msg = "Notícia Excluida com Sucesso!"
    except:
        msg = "Erro ao Excluir a Notícia!"
    return HttpResponseRedirect("/admin/noticia/listagem/?msg=%s" % msg)