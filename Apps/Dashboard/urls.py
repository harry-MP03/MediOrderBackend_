from django.urls import path, include

urlpatterns = [

        path ('H_PEDIDOSPACIENTE/', include('Apps.Dashboard.Fact_PedidoPaciente.urls')),
]
