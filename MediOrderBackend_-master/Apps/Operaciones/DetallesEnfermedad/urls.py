from django.urls import path
from .views import EnfermedadPromedio_PatientsAPIview

urlpatterns =\
[
    path("DetallesEnfermedades-PromedioEnfermedad/", EnfermedadPromedio_PatientsAPIview.as_view()), #Obtener el promedio de las enfermedades
]
