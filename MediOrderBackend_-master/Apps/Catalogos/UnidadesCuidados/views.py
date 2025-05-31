from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from config.utils.Pagination import PaginationMixin
from .models import Careunit
from .serializers import CareunitSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

from django.db.models import Avg

# Configuracion de el logger
logger = logging.getLogger(__name__)

class CareunitApiView(PaginationMixin, APIView):

    model = Careunit

    @swagger_auto_schema(responses={200: CareunitSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las unidades de cuidado
        """

        logger.info("GET request to list all Care units")
        UnidadCuidado = Careunit.objects.all().order_by('idCareunit')
        page = self.paginate_queryset(UnidadCuidado, request)

        if page is not None:
            serializer = CareunitSerializer(page, many=True)
            logger.info("Paginated response for Care units")
            return self.get_paginated_response(serializer.data)

        serializer = CareunitSerializer(UnidadCuidado, many=True)
        logger.error("Returning all care units without pagination")
        return Response(serializer.data)