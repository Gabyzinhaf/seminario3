from rest_framework import viewsets
from Funcionarios.models import funcionario
from Funcionarios.serializer import FuncionariosSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = FuncionariosSerializer