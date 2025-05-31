from django.urls import path
from .views import DiseasesApiView, Diseases_PPPD_ApiView

urlpatterns = [

    path("", DiseasesApiView.as_view()), #Listar Bebidas (Público)
    path('<int:pk>', Diseases_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)

]