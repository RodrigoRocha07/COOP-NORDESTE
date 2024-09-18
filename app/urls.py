from django.contrib import admin
from django.urls import path
from coop.views import *


urlpatterns = [
    path('', mostrar_home),
    path('sobre/', mostrar_sobre, name='sobre'),
    path('cadastro/',mostrar_cadastro, name='cadastro'),
    path('contato/',mostrar_contato, name='contato'),

]

# depois do barra
# funcao view
