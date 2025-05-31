from rest_framework.serializers import ModelSerializer, CharField

from .models import diseases

class DiseasesSerializer(ModelSerializer):
    tipoEnfermedad_Descripcion = CharField(source='typeDiseaseFK.nametype', read_only=True, label='Tipo de Enfermedad')

    class Meta:
        model = diseases
        fields = ['nameDisease', 'typeDiseaseFK','tipoEnfermedad_Descripcion']