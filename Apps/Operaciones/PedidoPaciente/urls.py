from django.urls import path

from .views import PedidoPacienteApiView, PedidoPaciente_PPPD_ApiView

urlpatterns = [

    path("", PedidoPacienteApiView.as_view()), #Listar los Pedidos
    path('<int:pk>', PedidoPaciente_PPPD_ApiView.as_view()), # POST, PATCH, PUT Y DELETE para los Pedidos

]