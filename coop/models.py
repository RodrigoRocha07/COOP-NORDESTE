from django.db import models
from datetime import timedelta
from django import forms
class Categorias(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    atribuição = models.CharField(max_length=255)
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']



class Locacao(models.Model):
    nome = models.CharField(max_length=255)
    categorias = models.ManyToManyField(Categorias, related_name='locacoes')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'
        ordering = ['nome']



class Cooperado(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    data_admissao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    locacao = models.ForeignKey(Locacao, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cooperado'
        verbose_name_plural = 'Cooperados'
        ordering = ['nome']



from decimal import Decimal
from django.db import models

class TurnoTrabalho(models.Model):
    cooperado = models.ForeignKey(Cooperado, on_delete=models.CASCADE, related_name='turnos')
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE, related_name='turnos')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='turnos')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)

    @property
    def horas_trabalhadas(self):
        delta = self.data_fim - self.data_inicio
        # Convertendo o delta para horas, usando Decimal para evitar problemas de tipo
        horas = Decimal(delta.total_seconds()) / Decimal(3600)
        return horas

    @property
    def valor_por_hora(self):
        return self.categoria.valor_pagamento

    @property
    def valor_total(self):
        return self.horas_trabalhadas * self.valor_por_hora

    def __str__(self):
        return f"Turno {self.data_inicio.strftime('%d/%m/%Y %H:%M')} - {self.data_fim.strftime('%d/%m/%Y %H:%M')} ({self.cooperado.nome})"

    class Meta:
        verbose_name = 'Turno de Trabalho'
        verbose_name_plural = 'Turnos de Trabalho'
        ordering = ['data_inicio']



class Pagamento(models.Model):
    cooperado = models.ForeignKey(Cooperado, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    referencia_turno = models.ForeignKey(TurnoTrabalho, on_delete=models.SET_NULL, null=True, blank=True, related_name='pagamentos')
    observacoes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.referencia_turno:
            self.valor = self.referencia_turno.valor_total
        super(Pagamento, self).save(*args, **kwargs)

    def __str__(self):
        return f"Pagamento de {self.valor} para {self.cooperado.nome} em {self.data_pagamento.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['data_pagamento']