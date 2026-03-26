
from django.db import models

class Licitacao(models.Model):
    numero = models.CharField(max_length=100)
    orgao = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()
    empresa_vencedora = models.CharField(max_length=255)

    def __str__(self):
        return self.numero
