from django.urls import path
from .views import AggregateCBApiView, AggregatesCB_PPPD_ApiView

urlpatterns = [

    path("", AggregateCBApiView.as_view()), #Listar Agregados (Público)
    path('<int:pk>', AggregatesCB_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los agregados (Con autenticacion JWT)

]