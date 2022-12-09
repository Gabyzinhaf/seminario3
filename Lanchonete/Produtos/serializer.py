from rest_framework import serializers
from Produtos.models import produto


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ['id', 'Nome', 'Tipo','Validade', 'Preco', 'Fabricacao']