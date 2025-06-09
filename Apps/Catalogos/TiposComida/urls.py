from django.urls import path
from .views import TipoComida_ApiView, TipoComida_PPPD_ApiView

urlpatterns = [

    path("", TipoComida_ApiView.as_view()), #Listar Tipos de comidas (Público)
    path('<int:pk>', TipoComida_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para Tipos de comidas

]