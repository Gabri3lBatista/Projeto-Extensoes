from django.contrib import admin

from .models import *

class GruposAdmin(admin.ModelAdmin):
    
    list_display = ['grupo', 'projeto', 'cliente', 'n_de_part', 'ver']
    search_fields =  ['grupo', 'projeto', 'cliente', 'n_de_part', 'ver']

admin.site.register(Grupos, GruposAdmin)