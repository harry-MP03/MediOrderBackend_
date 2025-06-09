from django.urls import path

from .views import (HistorialMedico_SoloActivosApiView, HistorialMedico_NoActivosApiView, ConteoActivosAPIView, \
    ConteoNoActivosAPIView, CamasDisponiblesAPIView, Listado_CamasDisponiblesAPIView, PatientActiveApiView,
    MedicalHistoryApiView, MedicalHistory_PPPD_ApiView)

urlpatterns = [

    path("SoloActivos", HistorialMedico_SoloActivosApiView.as_view()), #Listar Historiales Médicos solo activos
    path("NoActivos", HistorialMedico_NoActivosApiView.as_view()),  # Listar Historiales Médicos No activos
    path("Cantidad-Activos", ConteoActivosAPIView.as_view()),  #Obtener la cantidad total de activos
    path("Cantidad-NoActivos", ConteoNoActivosAPIView.as_view()),  # Obtener la cantidad total de no activos
    path("Cantidad-CamasDisponibles", CamasDisponiblesAPIView.as_view()),  # Obtener la cantidad total de camas disponibles
    path("Listado-CamasDisponibles", Listado_CamasDisponiblesAPIView.as_view()), #Obtener el listado de las camas disponibles
    path("Paciente-Activo", PatientActiveApiView.as_view()), #Listado de pacientes si son activos o no
    path("", MedicalHistoryApiView.as_view()), #Listado de Historiales Médicos
    path('<int:pk>', MedicalHistory_PPPD_ApiView.as_view()), # POST, PATCH, PUT Y DELETE para los Historiales Médicos

]