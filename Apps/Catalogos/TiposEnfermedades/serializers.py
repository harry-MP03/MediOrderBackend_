from rest_framework.serializers import ModelSerializer, CharField

from .models import Typedisease

class TypediseaseSerializer(ModelSerializer):
    class Meta:
        model = Typedisease
        fields = ['nametype']