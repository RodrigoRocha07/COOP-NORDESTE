from django.contrib import admin

from .models import Cooperado, Locação

@admin.register(Cooperado)
class CooperadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'telefone', 'email', 'data_admissao','locacao', 'ativo')
    search_fields = ('nome', 'cpf_cnpj')
    list_filter = ('ativo', 'data_admissao')

@admin.register(Locação)
class CooperadoLocação(admin.ModelAdmin):
    list_display = ('nome', 'categorias')
    search_fields = ('nome', 'categorias')
