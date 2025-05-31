from rest_framework.serializers import ModelSerializer, CharField

from .models import Careunit

class CareunitSerializer(ModelSerializer):
    class Meta:
        model = Careunit
        fields = ['nameCareUnit']