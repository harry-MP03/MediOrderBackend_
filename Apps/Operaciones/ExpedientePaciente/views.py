from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import expedientPatient
from .serializers import ExpedienteSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class Expediente_Paciente(PaginationMixin, APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = expedientPatient

    @swagger_auto_schema(responses={200: ExpedienteSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los expedientes e información sobre las enfermedades y condición de los pacientes
        """

        logger.info("GET request to list all Beverages")
        expediente = expedientPatient.objects.all().order_by('idExpedient')
        page = self.paginate_queryset(expediente, request)

        if page is not None:
            serializer = ExpedienteSerializer(page, many=True)
            logger.info("Paginated response for expedient")
            return self.get_paginated_response(serializer.data)

        serializer = ExpedienteSerializer(expediente, many=True)
        logger.error("Returning all expedients without pagination")
        return Response(serializer.data)