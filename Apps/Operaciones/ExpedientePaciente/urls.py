from django.urls import path

from .serializers import ExpedienteSerializer
from .views import Expediente_Paciente

urlpatterns = [

    path("", Expediente_Paciente.as_view()), #Listar los Expedientes

]