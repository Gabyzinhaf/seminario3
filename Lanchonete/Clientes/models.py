from django.db import models

class cliente(models.Model):
    Nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    Endereco = models.CharField(max_length=100)
    Cartao = models.CharField(max_length=50)
    Contato = models.CharField(max_length=11)

    def _str_(self):
        return self.Nome

# Create your models here.
