
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import foods
from .serializers import FoodSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

from django.db.models import Avg

# Configuracion de el logger
logger = logging.getLogger(__name__)

class FoodsApiView(PaginationMixin, APIView):

    model = foods

    @swagger_auto_schema(responses={200: FoodSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las comidas
        """

        logger.info("GET request to list all Foods")
        comidas = foods.objects.all().order_by('idFood')
        page = self.paginate_queryset(comidas, request)

        if page is not None:
            serializer = FoodSerializer(page, many=True)
            logger.info("Paginated response for Foods")
            return self.get_paginated_response(serializer.data)

        serializer = FoodSerializer(comidas, many=True)
        logger.error("Returning all foods without pagination")
        return Response(serializer.data)
