from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config.utils.Pagination import PaginationMixin
from .models import orderpatient
from .serializers import PedidoPacienteSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ...permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configuracion de el logger
logger = logging.getLogger(__name__)


class PedidoPacienteApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = orderpatient

    @swagger_auto_schema(responses={200: PedidoPacienteSerializer(many=True)})
    def get(self, request):
        """""
        Obtener todas los Pedidos
        """

        logger.info("GET request to list all Order")
        pedido = orderpatient.objects.all().order_by('idOrder')
        page = self.paginate_queryset(pedido, request)

        if page is not None:
            serializer = PedidoPacienteSerializer(page, many=True)
            logger.info("Paginated response for Order")
            return self.get_paginated_response(serializer.data)

        serializer = PedidoPacienteSerializer(pedido, many=True)
        logger.error("Returning all Order without pagination")
        return Response(serializer.data)


class PedidoPaciente_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = (IsAuthenticated,CustomPermission)
    model = orderpatient

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={201: PedidoPacienteSerializer(many=True)})
    def post(self, request):
        """""
        Ingresar un nuevo Pedido
        """
        logger.info("POST request to create a new Order")
        serializer = PedidoPacienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Order created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Order: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={200: PedidoPacienteSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar totalmente un Pedido especificando su ID
        """
        logger.info("PUT request to update Pedido with ID: %s", pk)
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        if not pedido:
            return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, pedido)  # Verificación de permisos
        serializer = PedidoPacienteSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Order updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update Order with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={200: PedidoPacienteSerializer(many=True)})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un Pedido por su ID.
        """
        logger.info("PATCH request to partially update Order with ID: %s", pk)
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        if not pedido:
            return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, pedido)  # Verificación de permisos
        serializer = PedidoPacienteSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Order partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update Order with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un Pedido por su ID.
        """
        logger.info("DELETE request to delete Order with ID: %s", pk)
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        if not pedido:
            return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, pedido)  # Verificación de permisos
        pedido.delete()
        logger.info("Order deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)