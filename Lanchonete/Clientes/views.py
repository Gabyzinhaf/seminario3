from rest_framework import viewsets
from Clientes.models import cliente
from Clientes.serializer import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer



