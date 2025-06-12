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
import logging.handlers

logger = logging.getLogger(__name__)


class PedidoPacienteApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = orderpatient

    @swagger_auto_schema(responses={200: PedidoPacienteSerializer(many=True)})
    def get(self, request):
        """
        Obtener todos los pedidos
        """
        logger.info("GET request to list all Orders")
        pedidos = orderpatient.objects.all().order_by('idOrder')
        page = self.paginate_queryset(pedidos, request)

        if page is not None:
            serializer = PedidoPacienteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PedidoPacienteSerializer(pedidos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={201: PedidoPacienteSerializer})
    def post(self, request):
        """
        Registrar un nuevo pedido
        """
        logger.info("POST request to create a new Order")
        serializer = PedidoPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Order created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Order: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PedidoPaciente_PPPD_ApiView(PaginationMixin, APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]
    model = orderpatient

    def get(self, request, pk):
        """
        Obtener un pedido por ID
        """
        logger.info("GET request for Order ID: %s", pk)
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        serializer = PedidoPacienteSerializer(pedido)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={200: PedidoPacienteSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un pedido
        """
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        serializer = PedidoPacienteSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Order updated (PUT) successfully")
            return Response(serializer.data)
        logger.error("Failed PUT update: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PedidoPacienteSerializer, responses={200: PedidoPacienteSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un pedido
        """
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        serializer = PedidoPacienteSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Order updated (PATCH) successfully")
            return Response(serializer.data)
        logger.error("Failed PATCH update: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un pedido
        """
        pedido = get_object_or_404(orderpatient, idOrder=pk)
        pedido.delete()
        logger.info("Order deleted successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)
