from rest_framework.serializers import ModelSerializer, CharField

from .models import beds

class BedSerializer(ModelSerializer):
    NombreUnidadCuidado = CharField(source='CareUnitFK.nameCareUnit', read_only=True, label='Nombre de Unidad de Cuidado')
    class Meta:
        model = beds
        fields = ['idbed' ,'bedCode', 'NombreUnidadCuidado']

class BedWriteSerializer(ModelSerializer):
    class Meta:
        model = beds
        # Incluye los campos que el frontend enviará para crear una cama
        fields = ['bedCode', 'CareUnitFK']