from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField

from .models import detailDisease
from Apps.Catalogos.Enfermedades.serializers import DiseasesSerializer

class DetailDiseaseSerializer(ModelSerializer):
    info_Enfermedad = DiseasesSerializer(source='diseaseFK', read_only=True)

    class Meta:
        model = detailDisease
        fields = ['info_Enfermedad']