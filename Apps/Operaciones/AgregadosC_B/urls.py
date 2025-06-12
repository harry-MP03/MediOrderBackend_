from django.urls import path
from .views import AggregateCBApiView, AggregatesCB_PPPD_ApiView, AggregatesLookupView

urlpatterns = [

    path("", AggregateCBApiView.as_view()), #Listar Agregados (Público)
    path("lookup", AggregatesLookupView.as_view()),
    path('<int:pk>', AggregatesCB_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para los agregados (Con autenticacion JWT)

]