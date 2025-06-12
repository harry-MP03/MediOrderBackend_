from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters

from config.utils.Pagination import PaginationMixin
from .models import systemAdmin
from .serializers import SystemAdminSerializer, SystemAdminLookupSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)

class SystemAdmin_ApiView(PaginationMixin, APIView):

    #permission_classes = [IsAuthenticated, CustomPermission]
    model = systemAdmin

    @swagger_auto_schema(responses={200: SystemAdminSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todos los Encargados del sistema
        """

        logger.info("GET request to list all Admins")
        systemadmin = systemAdmin.objects.all().order_by('idAdmin')
        page = self.paginate_queryset(systemadmin, request)

        if page is not None:
            serializer = SystemAdminSerializer(page, many=True)
            logger.info("Paginated response for Admin List")
            return self.get_paginated_response(serializer.data)

        serializer = SystemAdminSerializer(systemadmin, many=True)
        logger.error("Returning all Admin without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SystemAdminSerializer, responses={201: SystemAdminSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un Admin
        """
        logger.info("POST request to create a new Admin")
        serializer = SystemAdminSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Admin created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Admin: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SystemAdmin_PPPD_ApiView(PaginationMixin, APIView):

    #permission_classes = (IsAuthenticated,CustomPermission)
    model = systemAdmin
    @swagger_auto_schema(request_body=SystemAdminSerializer, responses={200: SystemAdminSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Admin especificando su ID
        """
        logger.info("PUT request to update Admin with ID: %s", pk)
        sysAdmin = get_object_or_404(systemAdmin, idAdmin=pk)
        if not sysAdmin:
            return Response({'error': 'Admin no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, sysAdmin)  # Verificación de permisos
        serializer = SystemAdminSerializer(sysAdmin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Admin updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Admin with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=SystemAdminSerializer, responses={200: SystemAdminSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Admin por su ID.
        """
        logger.info("PATCH request to partially update Admin with ID: %s", pk)
        sysAdmin = get_object_or_404(systemAdmin, idAdmin=pk)
        if not sysAdmin:
            return Response({'error': 'Admin no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, sysAdmin)  # Verificación de permisos
        serializer = SystemAdminSerializer(sysAdmin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Admin partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Admin with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Admin por su ID.
        """
        logger.info("DELETE request to delete Admin with ID: %s", pk)
        sysAdmin = get_object_or_404(systemAdmin, idAdmin=pk)
        if not sysAdmin:
            return Response({'error': 'Admin no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, sysAdmin)  # Verificación de permisos
        sysAdmin.delete()
        logger.info("Admin deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class SystemAdminLookupView(generics.ListAPIView):
    queryset = systemAdmin.objects.all()
    serializer_class = SystemAdminLookupSerializer
    pagination_class = None  # Nos aseguramos de que no haya paginación

    # --- LÍNEAS CLAVE PARA LA BÚSQUEDA ---
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Username']

    # --- NUEVA CONFIGURACIÓN DE ORDENAMIENTO ---
    ordering_fields = ['idAdmin', 'Username']  # Campos por los que permitimos ordenar
    ordering = ['idAdmin']  # <-- Ordenamiento por defecto (alfabético)
