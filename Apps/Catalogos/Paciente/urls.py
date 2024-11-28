from django.urls import path
from .views import PatientApiView, Patient_PPPD_ApiView

urlpatterns = [

    path("", PatientApiView.as_view()), #Listar Bebidas (Público)
    path('<int:pk>', Patient_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)

]