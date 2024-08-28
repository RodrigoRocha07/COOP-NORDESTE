from django.db import models

class Locação(models.Model):
    nome = models.CharField(max_length=255)
    categorias = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cooperado(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    data_admissao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    # Relacionamento com Locacao (Um cooperado pode ter uma locação associada)
    locacao = models.ForeignKey(Locação, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cooperado'
        verbose_name_plural = 'Cooperados'
        ordering = ['nome']
