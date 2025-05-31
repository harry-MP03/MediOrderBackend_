from django.urls import path

from .views import HistorialMedico_SoloActivosApiView, HistorialMedico_NoActivosApiView, ConteoActivosAPIView, \
    ConteoNoActivosAPIView, CamasDisponiblesAPIView, Listado_CamasDisponiblesAPIView

urlpatterns = [

    path("SoloActivos", HistorialMedico_SoloActivosApiView.as_view()), #Listar Historiales Médicos solo activos
    path("NoActivos", HistorialMedico_NoActivosApiView.as_view()),  # Listar Historiales Médicos No activos
    path("Cantidad-Activos", ConteoActivosAPIView.as_view()),  #Obtener la cantidad total de activos
    path("Cantidad-NoActivos", ConteoNoActivosAPIView.as_view()),  # Obtener la cantidad total de no activos
    path("Cantidad-CamasDisponibles", CamasDisponiblesAPIView.as_view()),  # Obtener la cantidad total de camas disponibles
    path("Listado-CamasDisponibles", Listado_CamasDisponiblesAPIView.as_view()), #Obtener el listado de las camas disponibles
]