from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters

from config.utils.Pagination import PaginationMixin
from .models import patient
from .serializers import PatientSerializer, PacientesLookupsSerializers
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
import logging.handlers
from django.db.models import Avg

# Configuracion del logger
logger = logging.getLogger(__name__)

class PatientApiView(PaginationMixin, APIView):
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer(many=True)})
    def get(self, request):
        """
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
        logger.error("Returning all patients without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PatientSerializer, responses={201: PatientSerializer()})
    def post(self, request):
        """
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
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer()})
    def get(self, request, pk):
        """
        Obtener un solo paciente por su ID
        """
        logger.info("GET request to retrieve Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)
        serializer = PatientSerializer(paciente)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PatientSerializer, responses={200: PatientSerializer()})
    def put(self, request, pk):
        """
        Actualizar totalmente un paciente especificando su ID
        """
        logger.info("PUT request to update Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)

        self.check_object_permissions(request, paciente)
        serializer = PatientSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Patient updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update Patient with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PatientSerializer, responses={200: PatientSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un paciente por su ID.
        """
        logger.info("PATCH request to partially update Patient with ID: %s", pk)
        paciente = get_object_or_404(patient, idpatient=pk)

        self.check_object_permissions(request, paciente)
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

        self.check_object_permissions(request, paciente)
        paciente.delete()
        logger.info("Patient deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class Paciente_Edad_DescensoApiView(PaginationMixin, APIView):
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer(many=True)})
    def get(self, request):
        """
        Obtener todos los pacientes con la edad de mayor a menor
        """
        logger.info("GET request to list all Patients")
        Edad_Descenso = patient.objects.all().order_by('-agePatient')
        page = self.paginate_queryset(Edad_Descenso, request)

        if page is not None:
            serializer = PatientSerializer(page, many=True)
            logger.info("Paginated response for Patients")
            return self.get_paginated_response(serializer.data)

        serializer = PatientSerializer(Edad_Descenso, many=True)
        logger.error("Returning all patients without pagination")
        return Response(serializer.data)

class EdadPromedio_PatientsAPIview(PaginationMixin, APIView):
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer(many=True)})
    def get(self, request):
        """
        Obtener el promedio de edad de los pacientes.
        """
        logger.info("GET request to Age average")
        edad_Promedio = patient.objects.all().aggregate(Avg('agePatient'))['agePatient__avg']

        if edad_Promedio is None:
            edad_Promedio = 0
        else:
            edad_Promedio = round(edad_Promedio)

        return Response({'edad_Promedio': edad_Promedio})

class PatientsCountAPIview(PaginationMixin, APIView):
    model = patient

    @swagger_auto_schema(responses={200: PatientSerializer(many=True)})
    def get(self, request):
        """
        Contar los pacientes registrados
        """
        logger.info("GET request to Patient Count")
        CantidadTotal = patient.objects.count()
        return Response({'CantidadTotal': CantidadTotal})

class PacienteLookupsApiView(generics.ListAPIView):
    queryset = patient.objects.all()
    serializer_class = PacientesLookupsSerializers
    pagination_class = None

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['cedulaPatient']
    ordering_fields = ['idpatient', 'cedulaPatient']
    ordering = ['cedulaPatient']
