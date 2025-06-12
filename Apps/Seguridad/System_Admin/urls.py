from django.urls import path
from .views import SystemAdmin_ApiView, SystemAdmin_PPPD_ApiView

urlpatterns = [

    path("", SystemAdmin_ApiView.as_view()), #Listar Admins (Público)
    path('<int:pk>', SystemAdmin_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los Admins (Con autenticacion JWT)

]