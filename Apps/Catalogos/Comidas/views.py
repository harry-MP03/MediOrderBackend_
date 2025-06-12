from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters

from config.utils.Pagination import PaginationMixin
from .models import foods
from .serializers import ComidasSerializer, ComidasLookupsSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)


class ComidasApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = foods

    @swagger_auto_schema(responses={200: ComidasSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las comidas
        """

        logger.info("GET request to list all Foods")
        comida = foods.objects.all().order_by('idFood')
        page = self.paginate_queryset(comida, request)

        if page is not None:
            serializer = ComidasSerializer(page, many=True)
            logger.info("Paginated response for food")
            return self.get_paginated_response(serializer.data)

        serializer = ComidasSerializer(comida, many=True)
        logger.error("Returning all food without pagination")
        return Response(serializer.data)


class comidas_PPPD_ApiView(APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = foods

    @swagger_auto_schema(request_body=ComidasSerializer, responses={201: ComidasSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una nueva Comida
        """
        logger.info("POST request to create a new Food")
        serializer = ComidasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Food created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Food: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ComidasSerializer, responses={200: ComidasSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una Comida especificando su ID
        """
        logger.info("PUT request to update Food with ID: %s", pk)
        comida = get_object_or_404(foods, idFood=pk)
        if not comida:
            return Response({'error': 'Comida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, comida)  # Verificación de permisos
        serializer = ComidasSerializer(comida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Food updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Food with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ComidasSerializer, responses={200: ComidasSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una Comida por su ID.
        """
        logger.info("PATCH request to partially update food with ID: %s", pk)
        comida = get_object_or_404(foods, idFood=pk)
        if not comida:
            return Response({'error': 'Comida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, comida)  # Verificación de permisos
        serializer = ComidasSerializer(comida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Food partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Food with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una Comida por su ID.
        """
        logger.info("DELETE request to delete Food with ID: %s", pk)
        comida = get_object_or_404(foods, idFood=pk)
        if not comida:
            return Response({'error': 'comida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, comida)  # Verificación de permisos
        comida.delete()
        logger.info("Food deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComidasLookupView(generics.ListAPIView):

    queryset = foods.objects.all()
    serializer_class = ComidasLookupsSerializer
    pagination_class = None  # Nos aseguramos de que no haya paginación

    # --- LÍNEAS CLAVE PARA LA BÚSQUEDA ---
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['foodName']

    # --- NUEVA CONFIGURACIÓN DE ORDENAMIENTO ---
    ordering_fields = ['idFood', 'foodName']  # Campos por los que permitimos ordenar
    ordering = ['foodName']  # <-- Ordenamiento por defecto (alfabético)