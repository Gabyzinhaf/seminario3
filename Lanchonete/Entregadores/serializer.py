from rest_framework import serializers
from Entregadores.models import entregador


class EntregadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = entregador
        fields = ['id', 'Nome', 'Endereco','Veiculo', 'Placa', 'CNH']