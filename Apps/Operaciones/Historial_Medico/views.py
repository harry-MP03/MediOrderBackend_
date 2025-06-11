from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin

#Modelos Historial Medico y Camas
from .models import medical_History
from Apps.Catalogos.Camas.models import beds

from drf_yasg.utils import swagger_auto_schema

#Serializer de Historial Médico y Camas
from .serializers import MedicalHistorySerializer, PacienteActivoSerializer
from Apps.Catalogos.Camas.serializers import BedSerializer

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configuracion de el logger
logger = logging.getLogger(__name__)

class MedicalHistoryApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas los Historiales Médicos
        """

        logger.info("GET request to list all Medical History")
        historialMedico = medical_History.objects.all().order_by('idMedicalHistory')
        page = self.paginate_queryset(historialMedico, request)

        if page is not None:
            serializer = MedicalHistorySerializer(page, many=True)
            logger.info("Paginated response for Medical History")
            return self.get_paginated_response(serializer.data)

        serializer = MedicalHistorySerializer(historialMedico, many=True)
        logger.error("Returning all Medical History without pagination")
        return Response(serializer.data)


class MedicalHistory_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = medical_History

    @swagger_auto_schema(request_body=MedicalHistorySerializer, responses={201: MedicalHistorySerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un nuevo Historial Médico
        """
        logger.info("POST request to create a new Medical History")
        serializer = MedicalHistorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Medical History created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Medical History: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MedicalHistorySerializer, responses={200: MedicalHistorySerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Historial Médico especificando su ID
        """
        logger.info("PUT request to update Medical History with ID: %s", pk)
        historialMedico = get_object_or_404(medical_History, idMedicalHistory=pk)
        if not historialMedico:
            return Response({'error': 'Historial Médico no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, historialMedico)  # Verificación de permisos
        serializer = MedicalHistorySerializer(historialMedico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Medical History updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Medical History with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MedicalHistorySerializer, responses={200: MedicalHistorySerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Historial Médico por su ID.
        """
        logger.info("PATCH request to partially update Detail Disease with ID: %s", pk)
        historialMedico = get_object_or_404(medical_History, idDetailDisease=pk)
        if not historialMedico:
            return Response({'error': 'Historial Médico no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, historialMedico)  # Verificación de permisos
        serializer = MedicalHistorySerializer(historialMedico, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Medical History partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Medical History with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Historial Médico por su ID.
        """
        logger.info("DELETE request to delete Medical History with ID: %s", pk)
        historialMedico = get_object_or_404(medical_History, idMedicalHistory=pk)
        if not historialMedico:
            return Response({'error': 'Historial Médico no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, historialMedico)  # Verificación de permisos
        historialMedico.delete()
        logger.info("Medical History deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Listado de historiales médicos solo activos
class HistorialMedico_SoloActivosApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los Historiales donde solo se muestren a pacientes activos
        """

        logger.info("GET request to list all Medical history")
        historiales_activos = medical_History.objects.filter(active_Patient=True)
        page = self.paginate_queryset(historiales_activos, request)

        if page is not None:
            serializer = MedicalHistorySerializer(page, many=True)
            logger.info("Paginated response for Medical History")
            return self.get_paginated_response(serializer.data)

        serializer = MedicalHistorySerializer(historiales_activos, many=True)
        logger.error("Returning all Medical History without pagination")
        return Response(serializer.data)

#Listado de historiales médicos no activos
class HistorialMedico_NoActivosApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los Historiales donde solo se muestren a pacientes no activos
        """

        logger.info("GET request to list all Medical history")
        historiales_Noactivos = medical_History.objects.filter(active_Patient=False)
        page = self.paginate_queryset(historiales_Noactivos, request)

        if page is not None:
            serializer = MedicalHistorySerializer(page, many=True)
            logger.info("Paginated response for Medical History")
            return self.get_paginated_response(serializer.data)

        serializer = MedicalHistorySerializer(historiales_Noactivos, many=True)
        logger.error("Returning all Medical History without pagination")
        return Response(serializer.data)

class ConteoActivosAPIView(APIView):
    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """
        Contar los Historiales Activos registrados
        """

        logger.info("GET request to Medical History Count")
        CantidadActivo = medical_History.objects.filter(active_Patient=True).count()
        return Response({'Cantidad Total de activos': CantidadActivo})

class ConteoNoActivosAPIView(APIView):
    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """
        Contar los Historiales No Activos registrados
        """

        logger.info("GET request to Medical History Count")
        CantidadNoActivo = medical_History.objects.filter(active_Patient=False).count()
        return Response({'Cantidad Total de no Activos': CantidadNoActivo})

class CamasDisponiblesAPIView(APIView):
    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """
        Contar las camas disponibles incluyendo las que no están registradas en el historial medico
        """

        logger.info("GET request to Medical History and Beds Count")
        CantidadNoActivo = medical_History.objects.filter(active_Patient=False).count()
        CamasEnHistorial = medical_History.objects.all().values_list('bedFK', flat=True)
        Camas_NoIncluidas = beds.objects.exclude(idbed__in=CamasEnHistorial).count()
        total_CamasDisponibles = CantidadNoActivo + Camas_NoIncluidas
        return Response({
            'Cantidad Total de Historiales No Activos': CantidadNoActivo,
            'Cantidad de camas no incluídas': Camas_NoIncluidas,
            'Total de camas disponibles': total_CamasDisponibles
        })

class Listado_CamasDisponiblesAPIView(APIView):
    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History, beds

    @swagger_auto_schema(responses={200: MedicalHistorySerializer(many=True)})
    def get(self, request):
        """
        Listar las camas disponibles incluyendo las que no están agregadas al registro de un historial médico
        """

        Camas_EnHistorial = medical_History.objects.all().values_list('bedFK', flat=True)
        Camas_NoIncluidas = beds.objects.exclude(idbed__in=Camas_EnHistorial)
        camas_pacientesNoActivos = beds.objects.filter(historiales_medicos__active_Patient=False)
        CamasDispobles_ = Camas_NoIncluidas.union(camas_pacientesNoActivos)

        serializer = BedSerializer(CamasDispobles_, many=True)

        return Response(serializer.data)

#ApiView del paciente si es activo o no
class PatientActiveApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = medical_History

    @swagger_auto_schema(responses={200: PacienteActivoSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los Historiales donde solo se muestren a pacientes activos
        """

        logger.info("GET request to list all Medical history")
        pacientes_activos = medical_History.objects.all().order_by('idMedicalHistory')
        page = self.paginate_queryset(pacientes_activos, request)

        if page is not None:
            serializer = PacienteActivoSerializer(page, many=True)
            logger.info("Paginated response for Medical History")
            return self.get_paginated_response(serializer.data)

        serializer = PacienteActivoSerializer(pacientes_activos, many=True)
        logger.error("Returning all Medical History without pagination")
        return Response(serializer.data)
