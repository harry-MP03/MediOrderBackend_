from django.urls import path
from .views import BebidasApiView

urlpatterns = [

    path("", BebidasApiView.as_view()), #Listar o crear Bebidas

]
