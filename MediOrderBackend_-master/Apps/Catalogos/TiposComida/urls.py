from django.urls import path
from .views import TypeFoodApiView

urlpatterns = [

    path("", TypeFoodApiView.as_view()), #Listar Tipos de comidas (Público)
]