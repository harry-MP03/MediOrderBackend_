from rest_framework.serializers import ModelSerializer

from .models import Careunit

class CareunitSerializer(ModelSerializer):
    class Meta:
        model = Careunit
        fields = ['idCareunit', 'nameCareUnit']