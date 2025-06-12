from django.urls import path
from .views import SystemAdmin_ApiView, SystemAdmin_PPPD_ApiView, SystemAdminLookupView

urlpatterns = [

    path("", SystemAdmin_ApiView.as_view()), #Listar Admins (Público)
    path("lookup", SystemAdminLookupView.as_view()),
    path('<int:pk>', SystemAdmin_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los Admins (Con autenticacion JWT)

]