from django.urls import path
from .views import BebidasApiView

app_name = "Bebidas"
urlpatterns = [

    path("", BebidasApiView.as_view(), name="Bebidas"),

]
