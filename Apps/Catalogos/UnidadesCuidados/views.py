from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters

from config.utils.Pagination import PaginationMixin
from .models import Careunit
from .serializers import CareunitSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)


class UnidadCuidadoApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = Careunit

    @swagger_auto_schema(responses={200: CareunitSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las unidades de cuidados
        """

        logger.info("GET request to list all Care Unit")

        unidadcuidado = Careunit.objects.all().order_by('idCareunit')
        page = self.paginate_queryset(unidadcuidado, request)

        if page is not None:
            serializer = CareunitSerializer(page, many=True)
            logger.info("Paginated response for Care Unit")
            return self.get_paginated_response(serializer.data)

        serializer = CareunitSerializer(unidadcuidado, many=True)
        logger.error("Returning all Care Unit without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CareunitSerializer, responses={201: CareunitSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una nueva unidades de cuidados
        """
        logger.info("POST request to create a new Care Unit")
        serializer = CareunitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Care Unit created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Care Unit: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnidadCuidado_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = Careunit

    @swagger_auto_schema(request_body=CareunitSerializer, responses={200: CareunitSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una unidad de cuidado especificando su ID
        """
        logger.info("PUT request to update Care Unit with ID: %s", pk)
        unidadcuidado = get_object_or_404(Careunit, idCareunit=pk)
        if not unidadcuidado:
            return Response({'error': 'Unidad de cuidado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, unidadcuidado)  # Verificación de permisos
        serializer = CareunitSerializer(unidadcuidado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Care Unit updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Care Unit with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CareunitSerializer, responses={200: CareunitSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una unidad de cuidado por su ID.
        """
        logger.info("PATCH request to partially update Care Unit with ID: %s", pk)
        unidadcuidado = get_object_or_404(Careunit, idCareunit=pk)
        if not unidadcuidado:
            return Response({'error': 'Cama no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, unidadcuidado)  # Verificación de permisos
        serializer = CareunitSerializer(unidadcuidado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Care Unit partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Care Unit with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una unidad de cuidado por su ID.
        """
        logger.info("DELETE request to delete Care Unit with ID: %s", pk)
        unidadcuidado = get_object_or_404(Careunit, idCareunit=pk)
        if not unidadcuidado:
            return Response({'error': 'unidad de cuidado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, unidadcuidado)  # Verificación de permisos
        unidadcuidado.delete()
        logger.info("Care Unit deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnidadCuidadoLookupView(APIView): #Cambiar a ApiView si es selectivo o generics.ListAPIView si es filtro
    """
    Una vista simple que devuelve TODAS las unidades de cuidado sin paginación,
    ideal para rellenar selectores o dropdowns en el frontend.
    """

    def get(self, request):
        # Obtenemos todos los objetos, sin paginación
        unidades = Careunit.objects.all().order_by('nameCareUnit')

        serializer = CareunitSerializer(unidades, many=True)
        return Response(serializer.data)
    """"""""""
    Devuelve TODAS las unidades de cuidado y permite la búsqueda y el ordenamiento.
    - Búsqueda: ?search=...
    - Ordenamiento: ?ordering=...
    """""""""""

    """""""""""
    def get(self, request):

    queryset = Careunit.objects.all()
    serializer_class = CareunitSerializer
    pagination_class = None  # Nos aseguramos de que no haya paginación

    # --- LÍNEAS CLAVE PARA LA BÚSQUEDA ---
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nameCareUnit']

    # --- NUEVA CONFIGURACIÓN DE ORDENAMIENTO ---
    ordering_fields = ['idCareunit', 'nameCareUnit']  # Campos por los que permitimos ordenar
    ordering = ['nameCareUnit']  # <-- Ordenamiento por defecto (alfabético)

    """""""""""


