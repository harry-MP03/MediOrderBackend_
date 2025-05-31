from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import Typedisease
from .serializers import TypediseaseSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class TypeDisease_ApiView(PaginationMixin, APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Typedisease

    @swagger_auto_schema(responses={200: TypediseaseSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los tipos de enfermedades
        """

        logger.info("GET request to list all Type diseases")
        tipoenfermedad = Typedisease.objects.all().order_by('idtype')
        page = self.paginate_queryset(tipoenfermedad, request)

        if page is not None:
            serializer = TypediseaseSerializer(page, many=True)
            logger.info("Paginated response for type disease")
            return self.get_paginated_response(serializer.data)

        serializer = TypediseaseSerializer(tipoenfermedad, many=True)
        logger.error("Returning all Types diseases without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TypediseaseSerializer, responses={201: TypediseaseSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un tipo de enfermedad nueva
        """
        logger.info("POST request to create a new Type Disease")
        serializer = TypediseaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Type Disease created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create TypeDisease: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDisease_PPPD_ApiView(APIView):

    permission_classes = (IsAuthenticated,CustomPermission)
    model = Typedisease
    @swagger_auto_schema(request_body=TypediseaseSerializer, responses={200: TypediseaseSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un tipo de enfermedad especificando su ID
        """
        logger.info("PUT request to update Type Disease with ID: %s", pk)
        tipoenfermedad = get_object_or_404(Typedisease, idtype=pk)
        if not tipoenfermedad.is_enfermedad:
            return Response({'error': 'Tipo de enfermedad no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoenfermedad)  # Verificación de permisos
        serializer = TypediseaseSerializer(tipoenfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Type Disease updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Type Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TypediseaseSerializer, responses={200: TypediseaseSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un tipo de enfermedad por su ID.
        """
        logger.info("PATCH request to partially update Type Disease with ID: %s", pk)
        tipoenfermedad = get_object_or_404(Typedisease, idtype=pk)
        if not tipoenfermedad:
            return Response({'error': 'Tipo de enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoenfermedad)  # Verificación de permisos
        serializer = TypediseaseSerializer(tipoenfermedad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Type Disease partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Type Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un tipo de enfermedad por su ID.
        """
        logger.info("DELETE request to delete TypeBeverage with ID: %s", pk)
        tipoenfermedad = get_object_or_404(Typedisease, idtype=pk)
        if not tipoenfermedad:
            return Response({'error': 'Tipo de enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipoenfermedad)  # Verificación de permisos
        tipoenfermedad.delete()
        logger.info("Type Disease deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)