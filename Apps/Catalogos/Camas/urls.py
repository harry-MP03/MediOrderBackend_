from django.urls import path
from .views import CamasApiView, camas_PPPD_ApiView

urlpatterns = [

    path("", CamasApiView.as_view()), #Listar Camas (Público)
    path('<int:pk>', camas_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las Camas

]