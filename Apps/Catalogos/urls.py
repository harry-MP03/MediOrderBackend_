from django.urls import path, include

urlpatterns = [

    path ('Bebidas/', include('Apps.Catalogos.Bebidas.urls')),
    path('Condicion/', include('Apps.Catalogos.Condicion.urls')),
    path('Paciente/', include('Apps.Catalogos.Paciente.urls')),
    path('Enfermedades/', include('Apps.Catalogos.Enfermedades.urls')),
    path('TiposEnfermedades/', include('Apps.Catalogos.TiposEnfermedades.urls')),
    path('Camas/', include('Apps.Catalogos.Camas.urls')),
    path('Comidas/', include('Apps.Catalogos.Comidas.urls')),
    path('TiposBebida/', include('Apps.Catalogos.TiposBebida.urls')),
    path('TiposComida/', include('Apps.Catalogos.TiposComida.urls')),
    path('UnidadesCuidados/', include('Apps.Catalogos.UnidadesCuidados.urls')),

]
