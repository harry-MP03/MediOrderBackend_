from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import H_PEDIDOS_PACIENTE_DEST
from .serializers import ReporteUnidades2025Serializer, ReporteCantidadTotal_2025_2024Serializer
from .serializers import Reporte_CantidadTotal_Meses2025Serializer

from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin

from django.db.models import Sum
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class ReportePedidosUnidad2025ApiView(APIView):

    @swagger_auto_schema (responses={200: ReporteUnidades2025Serializer(many=True)})
    def get(self, request):
        logger.info("Iniciando reporte de pedidos por unidad para el año 2025.")

        try:
            reporte_data = H_PEDIDOS_PACIENTE_DEST.objects.using('ETL').filter(
                Result_TiempoKey__Anio=2025
            ).values(
                'idMedicalHistory__NameCareUnit'
            ).annotate(
                cantidad_total=Sum('quantity')
            ).order_by(
                '-cantidad_total'
            )

            data_list = [
                {
                    'NombreUnidadCuidado': item['idMedicalHistory__NameCareUnit'],
                    'CantidadTotalPedidos': item['cantidad_total'],
                    'Anio': 2025
                }
                for item in reporte_data
            ]

            serializer = ReporteUnidades2025Serializer(data_list, many=True)
            logger.info("Reporte generado exitosamente.")
            return Response(serializer.data)

        except Exception as e:
            logger.error(f"Error generando el reporte de pedidos por unidad: {e}", exc_info=True)
            return Response(
                {"error": "Ocurrió un error interno al procesar la solicitud."},
                status=500
            )

class ReporteTotalPedidosPorAnioApiView(APIView):

    @swagger_auto_schema(
        operation_summary="Reporte de Cantidad Total de Pedidos por Año",
        operation_description="Muestra la cantidad total de pedidos para los años 2024 y 2025.",
        responses={200: ReporteCantidadTotal_2025_2024Serializer(many=True)}
    )
    def get(self, request):
        logger.info("Iniciando reporte de total de pedidos para los años 2024 y 2025.")

        try:
            # Se filtra agregando los años 2025 y 2024
            años_filtrar = [2024, 2025]

            # 1. Filtra los pedidos que pertenecen a los años en la lista.
            # 2. Agrupa los resultados por el año.
            # 3. Anota (calcula) la suma total de 'quantity' para cada año.
            reporte_data = H_PEDIDOS_PACIENTE_DEST.objects.using('ETL').filter(
                Result_TiempoKey__Anio__in=años_filtrar
            ).values(
                'Result_TiempoKey__Anio'  # Campo para agrupar
            ).annotate(
                total_pedidos=Sum('quantity')  # Campo calculado
            ).order_by(
                'Result_TiempoKey__Anio'  # Ordena por año
            )

            # Renombramos las claves para que coincidan con nuestro serializador
            data_list = [
                {
                    'Anio': item['Result_TiempoKey__Anio'],
                    'Cantidad_TotalPedidos': item['total_pedidos']
                }
                for item in reporte_data
            ]

            serializer = ReporteCantidadTotal_2025_2024Serializer(data_list, many=True)
            logger.info("Reporte anual de pedidos generado exitosamente.")
            return Response(serializer.data)

        except Exception as e:
            logger.error(f"Error generando el reporte anual de pedidos: {e}", exc_info=True)
            return Response(
                {"error": "Ocurrió un error interno al procesar la solicitud."},
                status=500
            )

class Reporte_TotalPedidosMeses2025ApiView(APIView):

    @swagger_auto_schema (responses={200: Reporte_CantidadTotal_Meses2025Serializer(many=True)})
    def get(self, request):
        logger.info("Iniciando reporte de total de pedidos por mes del año 2025.")

        try:
            reporte_data = H_PEDIDOS_PACIENTE_DEST.objects.using('ETL').filter(
                Result_TiempoKey__Anio=2025
            ).values(
                'Result_TiempoKey__NombreMes',
                'Result_TiempoKey__MesNumero'
            ).annotate(
                cantidad_total_mes = Sum('quantity')
            ).order_by(
                'Result_TiempoKey__MesNumero'
            )

            data_list = [
                {
                    'mes': item['Result_TiempoKey__NombreMes'],
                    'Cantidad_TotalPedidos': item['cantidad_total_mes'],
                    'Anio': 2025
                }
                for item in reporte_data
            ]

            serializer = Reporte_CantidadTotal_Meses2025Serializer(data_list, many=True)
            logger.info("Reporte generado exitosamente.")
            return Response(serializer.data)

        except Exception as e:
            logger.error(f"Error generando el reporte de pedidos por unidad: {e}", exc_info=True)
            return Response(
                {"error": "Ocurrió un error interno al procesar la solicitud."},
                status=500
            )