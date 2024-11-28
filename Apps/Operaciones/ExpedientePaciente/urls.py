from django.urls import path

from .serializers import ExpedienteSerializer
from .views import Expediente_Paciente

urlpatterns = [

    path("", Expediente_Paciente.as_view()), #Listar Bebidas (Público)
    #path('<int:pk>', bebidas_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)

]