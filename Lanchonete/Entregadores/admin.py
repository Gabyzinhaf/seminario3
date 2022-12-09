from django.contrib import admin
from Entregadores.models import entregador

class Entregador(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Endereco','Veiculo', 'Placa', 'CNH')
    list_display_links = ('id', 'Nome', 'CNH')
    search_fields = ('Nome','CNH',)
admin.site.register(entregador, Entregador)
# Register your models here.
