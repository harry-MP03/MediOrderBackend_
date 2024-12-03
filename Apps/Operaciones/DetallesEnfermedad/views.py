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

#Sacar el promedio de las enfermedades diagnosticadas en el registro de los detalles de enfermedad
class EnfermedadPromedio_PatientsAPIview(PaginationMixin, APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
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

