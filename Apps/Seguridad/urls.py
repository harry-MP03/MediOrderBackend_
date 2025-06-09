from django.urls import path, include

urlpatterns = [

    path('Usuarios/', include('Apps.Seguridad.Usuarios.urls')),
    path('System_Admin/', include('Apps.Seguridad.System_Admin.urls')),
]
