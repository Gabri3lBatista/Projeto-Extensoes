from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from .models import *

# Create your views here.
def index(request):
    template_name = 'index.html'
    
    try:
        email = request.session["email"]
        nome = request.session["nome"]
    except:
        pass
    return TemplateResponse(request, template_name, locals())