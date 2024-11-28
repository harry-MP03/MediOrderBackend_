from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import patient
from .serializers import PatientSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class PatientApiView(PaginationMixin, APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los pacientes
        """

        logger.info("GET request to list all Patients")
        paciente = patient.objects.all().order_by('idpatient')
        page = self.paginate_queryset(paciente, request)

        if page is not None:
            serializer = PatientSerializer(page, many=True)
            logger.info("Paginated response for Patients")
            return self.get_paginated_response(serializer.data)

        serializer = PatientSerializer(paciente, many=True)
        logger.error("Returning all beverages without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PatientSerializer, responses={201: PatientSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un paciente nuevo
        """
        logger.info("POST request to create a new Patient")
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Patient created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Patient: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Patient_PPPD_ApiView(APIView):

    permission_classes = (IsAuthenticated,CustomPermission)
    model = patient
    @swagger_auto_schema(request_body=PatientSerializer, responses={200: PatientSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un paciente especificando su ID
        """
        logger.info("PUT request to update Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)
        if not paciente:
            return Response({'error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, paciente)  # Verificación de permisos
        serializer = PatientSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Patient updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Patient with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PatientSerializer, responses={200: PatientSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un paciente por su ID.
        """
        logger.info("PATCH request to partially update Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)
        if not paciente:
            return Response({'error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, paciente)  # Verificación de permisos
        serializer = PatientSerializer(paciente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Patient partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Patient with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un paciente por su ID.
        """
        logger.info("DELETE request to delete Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)
        if not paciente:
            return Response({'error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, paciente)  # Verificación de permisos
        paciente.delete()
        logger.info("Patient deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
