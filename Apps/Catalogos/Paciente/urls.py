from django.urls import path
from .views import (
    PatientApiView,
    Patient_PPPD_ApiView,
    Paciente_Edad_DescensoApiView,
    EdadPromedio_PatientsAPIview,
    PatientsCountAPIview,
    PacienteLookupsApiView
)

urlpatterns = [
    path("", PatientApiView.as_view()),  # GET y POST para todos los pacientes
    path("<int:pk>/", Patient_PPPD_ApiView.as_view()),  # GET, PUT, PATCH, DELETE por ID
    path("Edad-Descenso/", Paciente_Edad_DescensoApiView.as_view()),  # Lista por edad descendente
    path("Edad-Promedio/", EdadPromedio_PatientsAPIview.as_view()),  # Promedio de edad
    path("Pacientes-Contados/", PatientsCountAPIview.as_view()),  # Conteo total
    path("lookup/", PacienteLookupsApiView.as_view()),  # Búsqueda por cédula
]
