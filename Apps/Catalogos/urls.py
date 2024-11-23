from django.urls import path, include

urlpatterns = [

    path ('Bebidas/', include('Apps.Catalogos.Bebidas.urls')),

]
