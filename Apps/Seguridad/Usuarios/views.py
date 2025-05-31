from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import User_CreateSerializer
from drf_yasg.utils import swagger_auto_schema

class UserCreateAPIView(APIView):
    @swagger_auto_schema(request_body=User_CreateSerializer)
    def post(self, request):
     serializer = User_CreateSerializer(data=request.data)

     if serializer.is_valid():
        serializer.save()
        return Response({"message": "¡El usuario ha sido creado exitosamente!"}, status=status.HTTP_201_CREATED)

     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)