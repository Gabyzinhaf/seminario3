from django.db import models

class fornecedor(models.Model):
    Nome = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=15)
    Contato = models.CharField(max_length=11)
    Produto = models.CharField(max_length=100)
    Quantidade = models.CharField(max_length=10)
    

    def _str_(self):
        return self.Nome
# Create your models here.
