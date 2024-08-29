from django.contrib import admin

from .models import *

@admin.register(Cooperado)
class CooperadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'telefone', 'email', 'data_admissao','locacao', 'ativo')
    search_fields = ('nome', 'cpf_cnpj')
    list_filter = ('ativo', 'data_admissao')

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'listar_categorias')

    def listar_categorias(self, obj):
        return ", ".join([categoria.nome for categoria in obj.categorias.all()])

    listar_categorias.short_description = 'Categorias'

admin.site.register(Locacao, LocacaoAdmin)


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'atribuição', 'valor_pagamento')
    search_fields = ('nome', 'tipo')

@admin.register(TurnoTrabalho)
class TurnoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('cooperado', 'locacao', 'data_inicio', 'data_fim', 'mostrar_valor_total')
    search_fields = ('cooperado__nome', 'locacao__nome')
    list_filter = ('data_inicio', 'data_fim')
    ordering = ['data_inicio']

    def mostrar_valor_total(self, obj):
        return obj.valor_total

    mostrar_valor_total.short_description = 'Valor Total Recebido'

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('cooperado', 'valor', 'data_pagamento', 'referencia_turno')
    search_fields = ('cooperado__nome',)
    list_filter = ('data_pagamento',)
    ordering = ['data_pagamento']
