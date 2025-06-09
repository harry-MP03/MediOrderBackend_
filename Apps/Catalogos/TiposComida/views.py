from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import typefood
from .serializers import TipoComidaSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class TipoComida_ApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = typefood

    @swagger_auto_schema(responses={200: TipoComidaSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los tipos de comidas
        """

        logger.info("GET request to list all type foods")
        tipoComida = typefood.objects.all().order_by('idTypeFood')
        page = self.paginate_queryset(tipoComida, request)

        if page is not None:
            serializer = TipoComidaSerializer(page, many=True)
            logger.info("Paginated response for type foods List")
            return self.get_paginated_response(serializer.data)

        serializer = TipoComidaSerializer(tipoComida, many=True)
        logger.error("Returning all type foods without pagination")
        return Response(serializer.data)

class TipoComida_PPPD_ApiView(APIView):

    #permission_classes = (IsAuthenticated,CustomPermission)
    model = typefood

    @swagger_auto_schema(request_body=TipoComidaSerializer, responses={201: TipoComidaSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar nuevo Tipo de comida
        """
        logger.info("POST request to create a new type foods")
        serializer = TipoComidaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("type foods created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create type foods: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoComidaSerializer, responses={200: TipoComidaSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Tipo de comida especificando su ID
        """
        logger.info("PUT request to update type foods with ID: %s", pk)
        tipoComida = get_object_or_404(typefood, idTypeFood=pk)
        if not tipoComida:
            return Response({'error': 'Tipo de Comida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoComida)  # Verificación de permisos
        serializer = TipoComidaSerializer(tipoComida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("type foods updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Type Food with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoComidaSerializer, responses={200: TipoComidaSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Tipo de Comida por su ID.
        """
        logger.info("PATCH request to partially update Type Foods with ID: %s", pk)
        tipoComida = get_object_or_404(typefood, idTypeFood=pk)
        if not tipoComida:
            return Response({'error': 'Tipo de Comida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoComida)  # Verificación de permisos
        serializer = TipoComidaSerializer(tipoComida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Type Foods partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Type Foods with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Tipo de comida por su ID.
        """
        logger.info("DELETE request to delete Type Foods with ID: %s", pk)
        tipoComida = get_object_or_404(typefood, idTypeFood=pk)
        if not tipoComida:
            return Response({'error': 'condición no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoComida)  # Verificación de permisos
        tipoComida.delete()
        logger.info("Type Foods deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

