from rest_framework import viewsets
from Produtos.models import produto
from Produtos.serializer import ProdutosSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = ProdutosSerializer
