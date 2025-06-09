from rest_framework.serializers import ModelSerializer

from .models import typefood


class TipoComidaSerializer(ModelSerializer):
    class Meta:
        model = typefood
        fields = ['idTypeFood', 'description_typefood']