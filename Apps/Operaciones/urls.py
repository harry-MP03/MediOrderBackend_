from django.urls import path, include

urlpatterns = [

        path ('ExpedientePaciente/', include('Apps.Operaciones.ExpedientePaciente.urls')),

]
