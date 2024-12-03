from django.urls import path, include

urlpatterns = [

        path ('ExpedientePaciente/', include('Apps.Operaciones.ExpedientePaciente.urls')),
        path('DetallesEnfermedad/', include('Apps.Operaciones.DetallesEnfermedad.urls')),
        path('Historial_Medico/', include('Apps.Operaciones.Historial_Medico.urls')),
]
