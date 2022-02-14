from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('projetos/', include('apps.projetos.urls')),
    path('aulas/', include('apps.aulas.urls')),
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.usuario.urls')),
]
