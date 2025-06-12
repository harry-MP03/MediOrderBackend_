from django.urls import path
from .views import BebidasApiView, bebidas_PPPD_ApiView, BebidaLookupView

urlpatterns = [

    path("", BebidasApiView.as_view()), #Listar Bebidas (Público)
    path('<int:pk>', bebidas_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)
    path("lookup", BebidaLookupView.as_view()),
]
