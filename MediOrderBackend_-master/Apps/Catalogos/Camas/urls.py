from django.urls import path
from .views import BedsApiView

urlpatterns = [

    path("", BedsApiView.as_view()), #Listar Camas (Público)

]