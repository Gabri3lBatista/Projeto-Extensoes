from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Grupos

#serve para redirecionar pagina
from django.urls import reverse_lazy

def abertura(request):
    return render(request, "index.html")

# pagina cadastro - C
class GruposCad(CreateView):
    model = Grupos
    fields = ['grupo','projeto','cliente','n_de_part','descricao', 'tutorial', 'ver'] 
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')


class GruposListagem(ListView):
    model = Grupos
    template_name = 'cadastros/listar_cadastros.html'


class GruposUpdate(UpdateView):
    model = Grupos
    fields = "__all__" 
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

#pagina deletar - D
class GruposDelete(DeleteView):
    model = Grupos
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('listagem')
