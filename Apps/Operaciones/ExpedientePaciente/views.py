from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import expedientPatient
from .serializers import ExpedienteSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class Expediente_Paciente(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = expedientPatient

    @swagger_auto_schema(responses={200: ExpedienteSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los expedientes e información sobre las enfermedades y condición de los pacientes
        """

        logger.info("GET request to list all Expedients")
        expediente = expedientPatient.objects.all().order_by('idExpedient')
        page = self.paginate_queryset(expediente, request)

        if page is not None:
            serializer = ExpedienteSerializer(page, many=True)
            logger.info("Paginated response for expedient")
            return self.get_paginated_response(serializer.data)

        serializer = ExpedienteSerializer(expediente, many=True)
        logger.error("Returning all expedients without pagination")
        return Response(serializer.data)

class Expediente_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = expedientPatient

    @swagger_auto_schema(request_body=ExpedienteSerializer, responses={201: ExpedienteSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un Expediente nuevo
        """
        logger.info("POST request to create a new Expedient")
        serializer = ExpedienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Expedient created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Expedient: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ExpedienteSerializer, responses={200: ExpedienteSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Expediente especificando su ID
        """
        logger.info("PUT request to update Expedient  with ID: %s", pk)
        expediente = get_object_or_404(expedientPatient, idExpedient=pk)
        if not expediente:
            return Response({'error': 'Expediente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, expedientPatient)  # Verificación de permisos
        serializer = ExpedienteSerializer(expediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Expedient updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Expedient with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ExpedienteSerializer, responses={200: ExpedienteSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Expediente por su ID.
        """
        logger.info("PATCH request to partially update Expedient with ID: %s", pk)
        expediente = get_object_or_404(expedientPatient, idExpedient=pk)
        if not expediente:
            return Response({'error': 'Expediente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, expediente)  # Verificación de permisos
        serializer = ExpedienteSerializer(expediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Expedient partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Expedient with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Expediente por su ID.
        """
        logger.info("DELETE request to delete Expedient with ID: %s", pk)
        expediente = get_object_or_404(expedientPatient, idExpedient=pk)
        if not expediente:
            return Response({'error': 'Expediente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, expediente)  # Verificación de permisos
        expediente.delete()
        logger.info("Expedient deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
