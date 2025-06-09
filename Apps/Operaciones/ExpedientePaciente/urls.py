from django.urls import path

from .views import Expediente_Paciente, Expediente_PPPD_ApiView

urlpatterns = [

    path("", Expediente_Paciente.as_view()), #Listar los Expedientes
    path('<int:pk>', Expediente_PPPD_ApiView.as_view()), # POST, PATCH, PUT Y DELETE para los Expedientes

]