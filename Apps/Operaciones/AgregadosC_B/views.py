from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters

from config.utils.Pagination import PaginationMixin
from .models import aggregates_cb
from .serializers import AggregatesCbSerializer, AgreggatesWriteSerializer, AgreggatesLookupSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)


class AggregateCBApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = aggregates_cb

    @swagger_auto_schema(responses={200: AggregatesCbSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas los agregados
        """

        logger.info("GET request to list all Agreggates")
        agregado = aggregates_cb.objects.all().order_by('idAggregates')
        page = self.paginate_queryset(agregado, request)

        if page is not None:
            serializer = AggregatesCbSerializer(page, many=True)
            logger.info("Paginated response for Agreggates")
            return self.get_paginated_response(serializer.data)

        serializer = AggregatesCbSerializer(agregado, many=True)
        logger.error("Returning all Agreggates without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AgreggatesWriteSerializer, responses={201: AgreggatesWriteSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un nuevo Agregados
        """
        logger.info("POST request to create a new Aggregates")
        serializer = AgreggatesWriteSerializer(data=request.data)

        if serializer.is_valid():
            nueva_cama = serializer.save()
            logger.info("Aggregates created successfully")
            read_serializer = AggregatesCbSerializer(nueva_cama)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Aggregates: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AggregatesCB_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = aggregates_cb

    @swagger_auto_schema(request_body=AggregatesCbSerializer, responses={200: AggregatesCbSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Agregado especificando su ID
        """
        logger.info("PUT request to update Agreggates with ID: %s", pk)
        Agregado = get_object_or_404(aggregates_cb, idAggregates=pk)
        if not Agregado:
            return Response({'error': 'Agregado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, Agregado)  # Verificación de permisos
        serializer = AggregatesCbSerializer(Agregado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Agreggates updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Agreggates with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AggregatesCbSerializer, responses={200: AggregatesCbSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un agregado por su ID.
        """
        logger.info("PATCH request to partially update Agreggates with ID: %s", pk)
        Agregado = get_object_or_404(aggregates_cb, idAggregates=pk)
        if not Agregado:
            return Response({'error': 'Agregado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, Agregado)  # Verificación de permisos
        serializer = AggregatesCbSerializer(Agregado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Agreggates partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Agreggates with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un agregado por su ID.
        """
        logger.info("DELETE request to delete Agreggates with ID: %s", pk)
        Agregado = get_object_or_404(aggregates_cb, idAggregates=pk)
        if not Agregado:
            return Response({'error': 'Agregado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, Agregado)  # Verificación de permisos
        Agregado.delete()
        logger.info("Agreggates deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AggregatesLookupView(generics.ListAPIView):
    queryset = aggregates_cb.objects.all()
    serializer_class = AgreggatesLookupSerializer
    pagination_class = None  # Nos aseguramos de que no haya paginación

    # --- LÍNEAS CLAVE PARA LA BÚSQUEDA ---
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['codeAggregates']

    # --- NUEVA CONFIGURACIÓN DE ORDENAMIENTO ---
    ordering_fields = ['idAggregates', 'codeAggregates']  # Campos por los que permitimos ordenar
    ordering = ['idAggregates']  # <-- Ordenamiento por defecto (alfabético)