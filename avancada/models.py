from django.db import models
from datetime import datetime

class LeadAvancada(models.Model):
    nome = models.CharField(max_length = 50)
    # telefone = models.CharField(max_length = 20)
    # cpf_cnpj = models.CharField(max_length = 17)
    # concessionaria = models.CharField(max_length = 50)
    data = models.DateTimeField(default=datetime.now, blank=True)
    # email = models.CharField(max_length = 50)
    desnivel = models.IntegerField()
    vazao = models.IntegerField()
    potencia = models.IntegerField()
    mchs = models.IntegerField()
    dist_hidr = models.IntegerField()
    dist_eletr = models.IntegerField()
    modelo = models.CharField(max_length = 50)
    tipo_cabo = models.CharField(max_length =50)
    def __str__(self):
        return self.nome

class Bitola(models.Model):
    bitola = models.CharField(max_length = 50)
    corrente = models.CharField(max_length = 50)
    def __str__(self):
        return self.bitola

class Conexoe(models.Model):
    nome_conex = models.CharField(max_length = 50)
    k = models.CharField(max_length = 50)
    def __str__(self):
        return self.nome_conex