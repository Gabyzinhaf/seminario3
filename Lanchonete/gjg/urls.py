from django.contrib import admin
from django.urls import path, include
from Clientes.views import ClientesViewSet
from Entregadores.views import EntregadorViewSet
from Fornecedores.views import FornecedorViewSet
from Franquias.views import FranquiasViewSet
from Funcionarios.views import FuncionariosViewSet
from Produtos.views import ProdutosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Cliente', ClientesViewSet)
router.register(r'Entregador', EntregadorViewSet)
router.register(r'Fornecedor', FornecedorViewSet)
router.register(r'Franquias', FranquiasViewSet)
router.register(r'Funcionarios', FuncionariosViewSet)
router.register(r'Produtos', ProdutosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
