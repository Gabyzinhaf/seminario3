from django.contrib import admin
from Produtos.models import produto

class ProdutoS(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Tipo','Validade', 'Preco', 'Fabricacao')
    list_display_links = ('id', 'Nome', 'Tipo')
    search_fields = ('Nome','Tipo',)
admin.site.register(produto, ProdutoS)
# Register your models here.
