from django.urls import path
from .views import PatientApiView, Patient_PPPD_ApiView, Paciente_Edad_DescensoApiView, EdadPromedio_PatientsAPIview, PatientsCountAPIview

urlpatterns = [

    path("", PatientApiView.as_view()), #Listar Pacientes
    path("Edad-Descenso/", Paciente_Edad_DescensoApiView.as_view()), #Listar Todos los pacientes con edad de mayor a menor
    path("Edad-Promedio/", EdadPromedio_PatientsAPIview.as_view()), #Obtener el edad promedio de los pacientes
    path("Pacientes-Contados/", PatientsCountAPIview.as_view()), #Obtener el conteo total de los pacientes
    path('<int:pk>', Patient_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los pacientes (Con autenticacion JWT)

]