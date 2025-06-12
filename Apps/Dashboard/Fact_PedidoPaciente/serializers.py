from rest_framework import serializers

class ReporteUnidades2025Serializer(serializers.Serializer):
    """
        cantidad total de pedidos
        por cada unidad de cuidado 
    """
    NombreUnidadCuidado = serializers.CharField()
    CantidadTotalPedidos = serializers.IntegerField()
    Anio = serializers.IntegerField()

class ReporteCantidadTotal_2025_2024Serializer(serializers.Serializer):
    """
    Cantidad total de pedidos
    del 2025 y 2024
    """
    Cantidad_TotalPedidos = serializers.IntegerField()
    Anio = serializers.IntegerField()

class Reporte_CantidadTotal_Meses2025Serializer(serializers.Serializer):
    """
    Cantidad total de pedidos por mes
    del 2025
    """
    Cantidad_TotalPedidos = serializers.IntegerField()
    mes = serializers.CharField()
    Anio = serializers.IntegerField()