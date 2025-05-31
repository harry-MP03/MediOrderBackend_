from rest_framework.serializers import ModelSerializer, CharField

from .models import typefood

class TypefoodSerializer(ModelSerializer):
    class Meta:
        model = typefood
        fields = ['description_typefood']