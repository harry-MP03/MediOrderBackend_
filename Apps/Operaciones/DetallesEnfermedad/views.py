from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from drf_yasg.utils import swagger_auto_schema
from .models import detailDisease

from .serializers import DetailDiseaseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...Catalogos.Enfermedades.models import diseases
from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

from django.db.models import Avg

# Configuracion de el logger
logger = logging.getLogger(__name__)

class DetailsDiseaseApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = detailDisease

    @swagger_auto_schema(responses={200: DetailDiseaseSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas los detalles enfermedades
        """

        logger.info("GET request to list all Detail Disease")
        detalle_enfermedad = detailDisease.objects.all().order_by('idDetailDisease')
        page = self.paginate_queryset(detalle_enfermedad, request)

        if page is not None:
            serializer = DetailDiseaseSerializer(page, many=True)
            logger.info("Paginated response for Detail Disease")
            return self.get_paginated_response(serializer.data)

        serializer = DetailDiseaseSerializer(detalle_enfermedad, many=True)
        logger.error("Returning all Detail Disease without pagination")
        return Response(serializer.data)


class DetalleEnfermedad_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = detailDisease

    @swagger_auto_schema(request_body=DetailDiseaseSerializer, responses={201: DetailDiseaseSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un nuevo Detalle enfermedad
        """
        logger.info("POST request to create a new Detail Disease")
        serializer = DetailDiseaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Detail Disease created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Detail Disease: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DetailDiseaseSerializer, responses={200: DetailDiseaseSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Detalle enfermedad especificando su ID
        """
        logger.info("PUT request to update Detail Disease with ID: %s", pk)
        detalle_enfermedad = get_object_or_404(detailDisease, idDetailDisease=pk)
        if not detalle_enfermedad:
            return Response({'error': 'Detalle Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, detalle_enfermedad)  # Verificación de permisos
        serializer = DetailDiseaseSerializer(detalle_enfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Detail Disease updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Detail Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DetailDiseaseSerializer, responses={200: DetailDiseaseSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Detalle Enfermedad por su ID.
        """
        logger.info("PATCH request to partially update Detail Disease with ID: %s", pk)
        detalle_enfermedad = get_object_or_404(detailDisease, idDetailDisease=pk)
        if not detalle_enfermedad:
            return Response({'error': 'Detalle Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, detalle_enfermedad)  # Verificación de permisos
        serializer = DetailDiseaseSerializer(detalle_enfermedad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Detail Disease partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Detail Disease with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Detalle enfermedad por su ID.
        """
        logger.info("DELETE request to delete Detail Disease with ID: %s", pk)
        detalle_enfermedad = get_object_or_404(detailDisease, idDetailDisease=pk)
        if not detalle_enfermedad:
            return Response({'error': 'Detalle enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, detalle_enfermedad)  # Verificación de permisos
        detalle_enfermedad.delete()
        logger.info("Detail Disease deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

#Sacar el promedio de las enfermedades diagnosticadas en el registro de los detalles de enfermedad
class EnfermedadPromedio_PatientsAPIview(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = detailDisease

    def get(self, request):
        """
        Obtener el promedio de enfermedad de los pacientes.
        """

        logger.info("GET request to Disease average")
        enfermedad_promedio = detailDisease.objects.all().aggregate(Avg('diseaseFK'))['diseaseFK__avg']

        if enfermedad_promedio is None:
            enfermedad_promedio = 0
            nombre_Enfermedad = "No se han encontrado enfermedades registrados"

        else:
            enfermedad_promedio = round(enfermedad_promedio) #Se redondea la llave foránea de la enfermedad para evitar un resultado en decimal
            try:
                enfermedad = diseases.objects.get(idDisease=enfermedad_promedio)
                nombre_Enfermedad = enfermedad.nameDisease
            except diseases.DoesNotExist:
                nombre_Enfermedad = "No se han encontrado enfermedades registrados"

        return Response({
            'enfermedad_promedio': enfermedad_promedio,
            'nombre_Enfermedad': nombre_Enfermedad

        })

