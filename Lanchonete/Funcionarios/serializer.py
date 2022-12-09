from rest_framework import serializers
from Funcionarios.models import funcionario


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields = ['id', 'Nome', 'PIS','Cargo', 'Salario', 'Contato']