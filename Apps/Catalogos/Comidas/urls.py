from django.urls import path
from .views import ComidasApiView, comidas_PPPD_ApiView, ComidasLookupView

urlpatterns = [

    path("", ComidasApiView.as_view()), #Listar Comidas (Público)
    path('<int:pk>', comidas_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las Comidas
    path("lookup", ComidasLookupView.as_view()),
]