from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import beverages, typeBeverage
from .serializers import BeverageSerializer
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from ...permissions import CustomPermission
#from config.utils.Pagination import PaginationMixin


class BebidasApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = beverages

    @swagger_auto_schema(responses={200: BeverageSerializer(many=True)})
    def get(self, request):
        serializer = BeverageSerializer(beverages.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BeverageSerializer,responses={201: BeverageSerializer(many=True)})
    def post(self, request):
        serializer = BeverageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

