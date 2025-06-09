from django.urls import path, include

urlpatterns = [

        path ('ExpedientePaciente/', include('Apps.Operaciones.ExpedientePaciente.urls')),
        path('DetallesEnfermedad/', include('Apps.Operaciones.DetallesEnfermedad.urls')),
        path('Historial_Medico/', include('Apps.Operaciones.Historial_Medico.urls')),
        path('AgregadosC_B/', include('Apps.Operaciones.AgregadosC_B.urls')),
        path('PedidoPaciente/', include('Apps.Operaciones.PedidoPaciente.urls')),
]
