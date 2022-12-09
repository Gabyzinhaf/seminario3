from rest_framework import serializers
from Clientes.models import cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['id', 'Nome', 'CPF','Endereco', 'Cartao', 'Contato']
