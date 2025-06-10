from rest_framework import serializers

class ReporteUnidades2025Serializer(serializers.Serializer):
    """
        cantidad total de pedidos
        por cada unidad de cuidado 
    """
    NombreUnidadCuidado = serializers.CharField()
    CantidadTotalPedidos = serializers.IntegerField()
    Anio = serializers.IntegerField() 
