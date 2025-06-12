from django.urls import path
from .views import PedidoPacienteApiView, PedidoPaciente_PPPD_ApiView

urlpatterns = [
    path("", PedidoPacienteApiView.as_view()),              # GET (lista) y POST (nuevo pedido)
    path("<int:pk>/", PedidoPaciente_PPPD_ApiView.as_view())  # GET, PUT, PATCH, DELETE por ID
]
