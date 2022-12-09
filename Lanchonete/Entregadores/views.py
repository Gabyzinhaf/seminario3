from rest_framework import viewsets
from Entregadores.models import entregador
from Entregadores.serializer import EntregadorSerializer

class EntregadorViewSet(viewsets.ModelViewSet):
    queryset = entregador.objects.all()
    serializer_class = EntregadorSerializer
