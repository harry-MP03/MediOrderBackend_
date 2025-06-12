from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import beds
from .serializers import BedSerializer, BedWriteSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)


class CamasApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    permission_classes = [AllowAny]
    model = beds

    @swagger_auto_schema(responses={200: BedSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas las Camas y las unidades de cuidados
        asignadas
        """

        logger.info("GET request to list all Beds")
        camas = beds.objects.all().order_by('idbed')
        page = self.paginate_queryset(camas, request)

        if page is not None:
            serializer = BedSerializer(page, many=True)
            logger.info("Paginated response for bed")
            return self.get_paginated_response(serializer.data)

        serializer = BedSerializer(camas, many=True)
        logger.error("Returning all beds without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BedWriteSerializer, responses={201: BedWriteSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar una nueva Cama
        """
        logger.info("POST request to create a new Bed")
        print(">>> DATOS RECIBIDOS EN EL POST:", request.data)
        serializer = BedWriteSerializer(data=request.data)

        if serializer.is_valid():
            nueva_cama = serializer.save()
            logger.info("Bed created successfully")
            read_serializer = BedSerializer(nueva_cama)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Bed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class camas_PPPD_ApiView(APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = beds

    @swagger_auto_schema(request_body=BedSerializer, responses={200: BedSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente una Cama especificando su ID
        """
        logger.info("PUT request to update bed with ID: %s", pk)
        cama = get_object_or_404(beds, idbed=pk)
        if not cama:
            return Response({'error': 'Cama no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cama)  # Verificación de permisos
        serializer = BedSerializer(cama, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Bed updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Bed with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=BedSerializer, responses={200: BedSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una Cama por su ID.
        """
        logger.info("PATCH request to partially update bed with ID: %s", pk)
        cama = get_object_or_404(beds, idbed=pk)
        if not cama:
            return Response({'error': 'Cama no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cama)  # Verificación de permisos
        serializer = BedSerializer(cama, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Bed partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Bed with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una Cama por su ID.
        """
        logger.info("DELETE request to delete Bed with ID: %s", pk)
        cama = get_object_or_404(beds, idbed=pk)
        if not cama:
            return Response({'error': 'cama no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cama)  # Verificación de permisos
        cama.delete()
        logger.info("Bed deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

