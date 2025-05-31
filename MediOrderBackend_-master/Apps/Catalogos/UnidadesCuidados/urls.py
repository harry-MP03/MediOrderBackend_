from django.urls import path
from .views import CareunitApiView

urlpatterns = [

    path("", CareunitApiView.as_view()), #Listar Unidades de cuidados

]