from rest_framework.serializers import ModelSerializer, CharField

from .models import beds

class BedSerializer(ModelSerializer):
    NombreUnidadCuidado = CharField(source='CareUnitFK.nameCareUnit', read_only=True, label='Nombre de Unidad de Cuidado')
    class Meta:
        model = beds
        fields = ['bedCode', 'NombreUnidadCuidado']

class CamaSoporteSerializer(ModelSerializer):
    UnidadCuidado = CharField(source='CareUnitFK.nameCareUnit', read_only=True, label='Unidad de Cuidado')
    class Meta:
        model = beds
        fields = ['UnidadCuidado', 'bedCode']