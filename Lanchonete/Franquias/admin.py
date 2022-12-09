from django.contrib import admin
from Franquias.models import franquia

class FranquiaS(admin.ModelAdmin):
    list_display = ('id', 'NomeProprietario', 'CNPJ','Endereco', 'Email', 'Contato')
    list_display_links = ('id', 'NomeProprietario', 'Email')
    search_fields = ('NomeProprietario','Email',)
admin.site.register(franquia, FranquiaS)
# Register your models here.
