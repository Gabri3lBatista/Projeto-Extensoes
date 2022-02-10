from django.urls import path
from cadastros import views
from cadastros.views import GruposCad, GruposListagem, GruposUpdate, GruposDelete

urlpatterns = [
    path('', views.abertura , name='index'),
    path('cadastros/', GruposCad.as_view(), name='cadastro'),
    path('listagem/', GruposListagem.as_view(), name='listagem'),
    path('update/<int:pk>', GruposUpdate.as_view() , name='update'),
    path('deletar/<int:pk>', GruposDelete.as_view() , name='deletar'),    
]