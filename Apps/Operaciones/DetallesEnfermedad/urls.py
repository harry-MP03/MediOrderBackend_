from django.urls import path
from .views import (EnfermedadPromedio_PatientsAPIview, DetailsDiseaseApiView,
                    DetalleEnfermedad_PPPD_ApiView, DetailDiseaseLookupApiView)

urlpatterns =\
[
    path("DetallesEnfermedades-PromedioEnfermedad/", EnfermedadPromedio_PatientsAPIview.as_view()), #Obtener el promedio de las enfermedades
    path("", DetailsDiseaseApiView.as_view()), #Listar Detalles enfermedades
    path("", DetailsDiseaseApiView.as_view()),  # Listar Detalles enfermedades
    path('<int:pk>', DetalleEnfermedad_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los Detalles Enfermedades
    path("lookup/", DetailDiseaseLookupApiView.as_view()),
]
