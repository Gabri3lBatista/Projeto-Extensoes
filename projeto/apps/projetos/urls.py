from django.urls import path
from .views import *
from . import views

app_name = 'projetos'

urlpatterns = [
    path('cadastros/', GruposCad.as_view(), name='cadastro'),
    path('listagem/', GruposListagem.as_view(), name='listagem'),
    path('update/<int:pk>', GruposUpdate.as_view() , name='update'),
    path('dados_projetos/<int:pk>/', views.dados_projeto, name='dados'),
    path('deletar/<int:pk>', GruposDelete.as_view() , name='deletar'),   
    path('status/', GruposStatus.as_view() , name='status'),
    # path('dell_grupo', dell_grupo, name='dell_grupo'),
]