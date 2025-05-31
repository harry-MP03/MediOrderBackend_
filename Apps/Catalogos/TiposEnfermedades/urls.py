from django.urls import path
from .views import TypeDisease_ApiView, TypeDisease_PPPD_ApiView

urlpatterns = [

    path("", TypeDisease_ApiView.as_view()), #Listar Bebidas (Público)
    path('<int:pk>', TypeDisease_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)

]