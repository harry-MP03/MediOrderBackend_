from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import H_PEDIDOS_PACIENTE_DEST
from .serializers import ReporteUnidades2025Serializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin

from django.db.models import Sum
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class ReportePedidosUnidad2025ApiView(  APIView):

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