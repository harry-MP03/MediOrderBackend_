from django.urls import path
from .views import ReportePedidosUnidad2025ApiView, ReporteTotalPedidosPorAnioApiView

urlpatterns = [

    path("UnidadCuidado-CantidadTotal-2025", ReportePedidosUnidad2025ApiView.as_view()),
    path("Pedido-CantidadTotal-2025-2024", ReporteTotalPedidosPorAnioApiView.as_view()),

]