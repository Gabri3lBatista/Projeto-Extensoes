from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from .models import *

# Create your views here.
def index(request):
    template_name = 'index.html'
    
    try:
        id_usuario = request.session["id"]
        email_usuario = request.session["email"]
        nome_usuario = request.session["nome"]
    except:
        pass
    return TemplateResponse(request, template_name, locals())