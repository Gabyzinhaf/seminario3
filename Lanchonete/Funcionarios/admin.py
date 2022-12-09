from django.contrib import admin
from Funcionarios.models import funcionario

class FuncionarioS(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'PIS','Cargo', 'Salario', 'Contato')
    list_display_links = ('id', 'Nome', 'PIS')
    search_fields = ('Nome','PIS',)
admin.site.register(funcionario, FuncionarioS)
# Register your models here.
