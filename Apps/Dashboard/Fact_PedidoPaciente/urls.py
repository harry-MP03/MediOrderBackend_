from django.urls import path
from .views import ReportePedidosUnidad2025ApiView

urlpatterns = [

    path("UnidadCuidado-CantidadTotal-2025", ReportePedidosUnidad2025ApiView.as_view()),

]