from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'aulas'

urlpatterns = [
    path('', index, name='index'),
]
