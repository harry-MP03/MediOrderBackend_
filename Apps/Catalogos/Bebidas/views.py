from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import beverages
from .serializers import BeverageSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class BebidasApiView(PaginationMixin, APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = beverages

    @swagger_auto_schema(responses={200: BeverageSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las bebidas y los tipos de bebidas
        asignadas
        """

        logger.info("GET request to list all Beverages")
        bebidas = beverages.objects.all().order_by('idBeverages')
        page = self.paginate_queryset(bebidas, request)

        if page is not None:
            serializer = BeverageSerializer(page, many=True)
            logger.info("Paginated response for beverage")
            return self.get_paginated_response(serializer.data)

        serializer = BeverageSerializer(bebidas, many=True)
        logger.error("Returning all beverages without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BeverageSerializer, responses={201: BeverageSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una bebida nueva
        """
        logger.info("POST request to create a new Beverage")
        serializer = BeverageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Beverage created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create beverage: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class bebidas_PPPD_ApiView(APIView):

    permission_classes = (IsAuthenticated,CustomPermission)
    model = beverages
    @swagger_auto_schema(request_body=BeverageSerializer, responses={200: BeverageSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una bebida especificando su ID
        """
        logger.info("PUT request to update beverage with ID: %s", pk)
        bebida = get_object_or_404(beverages, idBeverages=pk)
        if not bebida:
            return Response({'error': 'Bebida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, bebida)  # Verificación de permisos
        serializer = BeverageSerializer(bebida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Beverage updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update beverage with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=BeverageSerializer, responses={200: BeverageSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una bebida por su ID.
        """
        logger.info("PATCH request to partially update beverage with ID: %s", pk)
        bebida = get_object_or_404(beverages, idBeverages=pk)
        if not bebida:
            return Response({'error': 'Bebida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, bebida)  # Verificación de permisos
        serializer = BeverageSerializer(bebida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("beverage partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update beverage with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una bebida por su ID.
        """
        logger.info("DELETE request to delete Beverage with ID: %s", pk)
        bebida = get_object_or_404(beverages, idBeverages=pk)
        if not bebida:
            return Response({'error': 'bebida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, bebida)  # Verificación de permisos
        bebida.delete()
        logger.info("Beverage deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

