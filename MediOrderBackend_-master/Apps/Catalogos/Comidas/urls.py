from django.urls import path
from .views import  FoodsApiView

urlpatterns = [

    path("", FoodsApiView.as_view()), #Listar Comidas (Público)

]