from django.urls import path
from .views import UnidadCuidadoApiView, UnidadCuidado_PPPD_ApiView, UnidadCuidadoLookupView

urlpatterns = [

    path("", UnidadCuidadoApiView.as_view()), #Listar Unidades de Cuidados (Público)
    path("lookup/", UnidadCuidadoLookupView.as_view()), #Listar Unidades de Cuidados (Público)
    path('<int:pk>', UnidadCuidado_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las Unidades de cuidados

]