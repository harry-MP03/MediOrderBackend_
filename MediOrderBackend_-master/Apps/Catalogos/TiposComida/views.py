from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import typefood
from .serializers import TypefoodSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

from django.db.models import Avg

# Configuracion de el logger
logger = logging.getLogger(__name__)

class TypeFoodApiView(PaginationMixin, APIView):

    model = typefood

    @swagger_auto_schema(responses={200: TypefoodSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los Tipos de comidas
        """

        logger.info("GET request to list all Type Foods")
        TipoComida = typefood.objects.all().order_by('idTypeFood')
        page = self.paginate_queryset(TipoComida, request)

        if page is not None:
            serializer = TypefoodSerializer(page, many=True)
            logger.info("Paginated response for Type Food")
            return self.get_paginated_response(serializer.data)

        serializer = TypefoodSerializer(TipoComida, many=True)
        logger.error("Returning all Type foods without pagination")
        return Response(serializer.data)
