from django.db import models
class franquia(models.Model):
    NomeProprietario = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=15)
    Endereco = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Contato = models.CharField(max_length=11)

    def _str_(self):
        return self.NomeProprietario

# Create your models here.
