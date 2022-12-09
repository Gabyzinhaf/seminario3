from django.contrib import admin
from Fornecedores.models import fornecedor

class FornecedoreS(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CNPJ','Contato', 'Produto', 'Quantidade')
    list_display_links = ('id', 'Nome', 'CNPJ')
    search_fields = ('Nome','CNPJ',)
admin.site.register(fornecedor, FornecedoreS)
# Register your models here.
