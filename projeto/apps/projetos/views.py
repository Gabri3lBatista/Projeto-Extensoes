from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Grupos

#serve para redirecionar pagina
from django.urls import reverse_lazy

def index(request):
    return render(request, "projetos/cadastro_projeto.html")

# pagina cadastro - C
class GruposCad(CreateView):
    model = Grupos
    fields = ['grupo','projeto','cliente','n_de_part','descricao', 'ver', 'status', 'dataIni', 'dataFim', 'tutorial'] 
    template_name = 'projetos/cadastro_projeto.html'
    success_url = reverse_lazy('projetos:listagem')


class GruposListagem(ListView):
    model = Grupos
    template_name = 'projetos/listagem_projeto.html'


class GruposUpdate(UpdateView):
    model = Grupos
    fields = "__all__" 
    template_name = 'projetos/cadastro_projeto.html'
    success_url = reverse_lazy('projetos:listagem')

#pagina deletar - D
class GruposDelete(DeleteView):
    model = Grupos
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('projetos:listagem')

class GruposStatus(ListView):
    model = Grupos
    template_name = 'cadastros/status_cadastros.html'
    success_url = reverse_lazy('projetos:listagem')



def dados_projeto(request, pk):
    a_list = Grupos.objects.filter(id=pk)
    context = {'dados': a_list}
    return render(request, 'projetos/dados_projeto.html', context)

# from django.http import HttpResponseRedirect
# from django.template.response import TemplateResponse

# from .models import *
# from ..usuario.views import verificacao
# # Create your views here.

# def index(request):
#     if verificacao(request):
#         email = request.session["email"]
#         nome = request.session["nome"]
        
#     template_name = 'projetos/index.html'
    
#     object_list = Grupos.objects.all()
    
#     return TemplateResponse(request, template_name, locals())

# def dell_grupo(request):
#     id_grupo = request.GET.get('id')
#     Grupos.objects.get(id= id_grupo).delete()
    
#     return HttpResponseRedirect('/projetos')

