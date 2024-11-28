from django.urls import path, include

urlpatterns = [

    path ('Bebidas/', include('Apps.Catalogos.Bebidas.urls')),
    path('Condicion/', include('Apps.Catalogos.Condicion.urls')),
    path('Paciente/', include('Apps.Catalogos.Paciente.urls')),
    path('Enfermedades/', include('Apps.Catalogos.Enfermedades.urls')),
    path('TiposEnfermedades/', include('Apps.Catalogos.TiposEnfermedades.urls')),

]
