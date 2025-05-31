from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import beds
from .serializers import BedSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

from django.db.models import Avg

# Configuracion de el logger
logger = logging.getLogger(__name__)

class BedsApiView(PaginationMixin, APIView):

    model = beds

    @swagger_auto_schema(responses={200: BedSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las camas
        """

        logger.info("GET request to list all Beds")
        cama = beds.objects.all().order_by('idbed')
        page = self.paginate_queryset(cama, request)

        if page is not None:
            serializer = BedSerializer(page, many=True)
            logger.info("Paginated response for Beds")
            return self.get_paginated_response(serializer.data)

        serializer = BedSerializer(cama, many=True)
        logger.error("Returning all beds without pagination")
        return Response(serializer.data)
