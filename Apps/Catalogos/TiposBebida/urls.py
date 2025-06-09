from django.urls import path
from .views import TipoBebida_ApiView, TipoBebida_PPPD_ApiView

urlpatterns = [

    path("", TipoBebida_ApiView.as_view()), #Listar Tipos de bebidas (Público)
    path('<int:pk>', TipoBebida_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para Tipos de bebidas

]