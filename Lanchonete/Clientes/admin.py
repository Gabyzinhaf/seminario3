from django.contrib import admin
from Clientes.models import cliente

class clienteS(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CPF','Endereco', 'Cartao', 'Contato')
    list_display_links = ('id', 'Nome', 'CPF')
    search_fields = ('Nome','CPF',)
admin.site.register(cliente, clienteS)
# Register your models here.
