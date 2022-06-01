from django.db import models
from datetime import datetime

class LeadBasica(models.Model):
    nome = models.CharField(max_length = 50)
    # telefone = models.CharField(max_length = 20)
    # cpf_cnpj = models.CharField(max_length = 17)
    # concessionaria = models.CharField(max_length = 50)
    # data = models.DateTimeField(default=datetime.now, blank=True)
    # email = models.CharField(max_length = 20)
    # modelo = models.CharField(max_length = 20)
    desnivel = models.IntegerField()
    vazao = models.IntegerField()
    potencia = models.IntegerField()
    mchs = models.IntegerField()
    def __str__(self):
        return self.nome
