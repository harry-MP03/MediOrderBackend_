from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import aggregates_cb
from .serializers import AggregatesCbSerializer
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


class AggregatesCB_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = aggregates_cb

    @swagger_auto_schema(request_body=AggregatesCbSerializer, responses={201: AggregatesCbSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un nuevo Agregados
        """
        logger.info("POST request to create a new Agreggates")
        serializer = AggregatesCbSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Agreggates created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Agreggates: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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