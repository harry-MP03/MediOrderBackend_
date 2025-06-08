from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import diseases
from .serializers import DiseasesSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class DiseasesApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = diseases

    @swagger_auto_schema(responses={200: DiseasesSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos las Enfermedades y los tipos de Enfermedades
        asignadas
        """

        logger.info("GET request to list all Diseases")
        enfermedad = diseases.objects.all().order_by('idDisease')
        page = self.paginate_queryset(enfermedad, request)

        if page is not None:
            serializer = DiseasesSerializer(page, many=True)
            logger.info("Paginated response for Diseases")
            return self.get_paginated_response(serializer.data)

        serializer = DiseasesSerializer(enfermedad, many=True)
        logger.error("Returning all Diseases without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DiseasesSerializer, responses={201: DiseasesSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una enfermedad nueva
        """
        logger.info("POST request to create a new Disease")
        serializer = DiseasesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Disease created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Disease: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Diseases_PPPD_ApiView(APIView):

    #permission_classes = (IsAuthenticated,CustomPermission)
    model = diseases
    @swagger_auto_schema(request_body=DiseasesSerializer, responses={200: DiseasesSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una Enfermedad especificando su ID
        """
        logger.info("PUT request to update Disease with ID: %s", pk)
        enfermedad = get_object_or_404(diseases, idDisease=pk)
        if not enfermedad:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, enfermedad)  # Verificación de permisos
        serializer = DiseasesSerializer(enfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Disease updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DiseasesSerializer, responses={200: DiseasesSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una Enfermedad por su ID.
        """
        logger.info("PATCH request to partially update Disease with ID: %s", pk)
        enfermedad = get_object_or_404(diseases, idDisease=pk)
        if not enfermedad:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, enfermedad)  # Verificación de permisos
        serializer = DiseasesSerializer(enfermedad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Disease partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una Enfermedad por su ID.
        """
        logger.info("DELETE request to delete Beverage with ID: %s", pk)
        enfermedad = get_object_or_404(diseases, idDisease=pk)
        if not enfermedad:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, enfermedad)  # Verificación de permisos
        enfermedad.delete()
        logger.info("Disease deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
