from django.db import models

class entregador(models.Model):
    Nome = models.CharField(max_length=50)
    Endereco = models.CharField(max_length=50)
    Veiculo = models.CharField(max_length=20)
    Placa = models.CharField(max_length=7)
    CNH = models.CharField(max_length=9)

    def _str_(self):
        return self.Nome
# Create your models here.
