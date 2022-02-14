import imp
from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
]
