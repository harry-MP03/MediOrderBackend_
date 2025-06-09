from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import typeBeverage
from .serializers import TypeBeverageSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class TipoBebida_ApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = typeBeverage

    @swagger_auto_schema(responses={200: TypeBeverageSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los tipos de bebidas
        """

        logger.info("GET request to list all type beverages")
        tipobebida = typeBeverage.objects.all().order_by('id_typeBeverage')
        page = self.paginate_queryset(tipobebida, request)

        if page is not None:
            serializer = TypeBeverageSerializer(page, many=True)
            logger.info("Paginated response for type beverages List")
            return self.get_paginated_response(serializer.data)

        serializer = TypeBeverageSerializer(tipobebida, many=True)
        logger.error("Returning all type beverages without pagination")
        return Response(serializer.data)

class TipoBebida_PPPD_ApiView(APIView):

    #permission_classes = (IsAuthenticated,CustomPermission)
    model = typeBeverage

    @swagger_auto_schema(request_body=TypeBeverageSerializer, responses={201: TypeBeverageSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una Condición nueva
        """
        logger.info("POST request to create a new type beverages")
        serializer = TypeBeverageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("type beverages created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create type beverages: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TypeBeverageSerializer, responses={200: TypeBeverageSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una Condición especificando su ID
        """
        logger.info("PUT request to update type beverages with ID: %s", pk)
        tipobebida = get_object_or_404(typeBeverage, id_typeBeverage=pk)
        if not tipobebida:
            return Response({'error': 'Tipo de Bebida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipobebida)  # Verificación de permisos
        serializer = TypeBeverageSerializer(tipobebida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("type beverages updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Type Beverages with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TypeBeverageSerializer, responses={200: TypeBeverageSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una Condición por su ID.
        """
        logger.info("PATCH request to partially update Type Beverages with ID: %s", pk)
        tipobebida = get_object_or_404(typeBeverage, id_typeBeverage=pk)
        if not tipobebida:
            return Response({'error': 'Condición no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipobebida)  # Verificación de permisos
        serializer = TypeBeverageSerializer(tipobebida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Type Beverages partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Type Beverages with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una condición por su ID.
        """
        logger.info("DELETE request to delete Type Beverages with ID: %s", pk)
        tipobebida = get_object_or_404(typeBeverage, id_typeBeverage=pk)
        if not tipobebida:
            return Response({'error': 'condición no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipobebida)  # Verificación de permisos
        tipobebida.delete()
        logger.info("Type Beverages deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
