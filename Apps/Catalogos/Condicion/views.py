from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import condition_lvl
from .serializers import ConditionSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class ConditionLvl_ApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = condition_lvl

    @swagger_auto_schema(responses={200: ConditionSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos las Condiciones
        """

        logger.info("GET request to list all Conditions")
        condicion = condition_lvl.objects.all().order_by('idcondition_lvl')
        page = self.paginate_queryset(condicion, request)

        if page is not None:
            serializer = ConditionSerializer(page, many=True)
            logger.info("Paginated response for Condition List")
            return self.get_paginated_response(serializer.data)

        serializer = ConditionSerializer(condicion, many=True)
        logger.error("Returning all Conditions without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ConditionSerializer, responses={201: ConditionSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una Condición nueva
        """
        logger.info("POST request to create a new Condition")
        serializer = ConditionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Condition created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Condition: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Condition_PPPD_ApiView(PaginationMixin, APIView):

    #permission_classes = (IsAuthenticated,CustomPermission)
    model = condition_lvl
    @swagger_auto_schema(request_body=ConditionSerializer, responses={200: ConditionSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una Condición especificando su ID
        """
        logger.info("PUT request to update Condition with ID: %s", pk)
        condicion = get_object_or_404(condition_lvl, idcondition_lvl=pk)
        if not condicion:
            return Response({'error': 'condicion no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, condicion)  # Verificación de permisos
        serializer = ConditionSerializer(condicion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Condition updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Condition with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ConditionSerializer, responses={200: ConditionSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una Condición por su ID.
        """
        logger.info("PATCH request to partially update Condition with ID: %s", pk)
        condicion = get_object_or_404(condition_lvl, idcondition_lvl=pk)
        if not condicion:
            return Response({'error': 'Condición no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, condicion)  # Verificación de permisos
        serializer = ConditionSerializer(condicion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Condition partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Condition with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una condición por su ID.
        """
        logger.info("DELETE request to delete condition with ID: %s", pk)
        condicion = get_object_or_404(condition_lvl, idcondition_lvl=pk)
        if not condicion:
            return Response({'error': 'condición no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, condicion)  # Verificación de permisos
        condicion.delete()
        logger.info("Condition deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
