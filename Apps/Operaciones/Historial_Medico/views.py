from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin

#Modelos Historial Medico y Camas
from .models import medical_History
from Apps.Catalogos.Camas.models import beds

from drf_yasg.utils import swagger_auto_schema

#Serializer de Historial Médico y Camas
from .serializers import MedicalHistorySerializer
from Apps.Catalogos.Camas.serializers import BedSerializer

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configuracion de el logger
logger = logging.getLogger(__name__)

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