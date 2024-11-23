from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import beverages
from .serializers import BeverageSerializer


class BebidasApiView(APIView):
    def get(self, request):
        serializer = BeverageSerializer(beverages.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)