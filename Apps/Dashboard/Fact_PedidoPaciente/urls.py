from django.urls import path
from .views import ReportePedidosUnidad2025ApiView, ReporteTotalPedidosPorAnioApiView, Reporte_TotalPedidosMeses2025ApiView

urlpatterns = [

    path("UnidadCuidado-CantidadTotal-2025", ReportePedidosUnidad2025ApiView.as_view()),
    path("Pedido-CantidadTotal-2025-2024", ReporteTotalPedidosPorAnioApiView.as_view()),
    path("Pedido-CantidadTotalPorMes-2025", Reporte_TotalPedidosMeses2025ApiView.as_view()),

]