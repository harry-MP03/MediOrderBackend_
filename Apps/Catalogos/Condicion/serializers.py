from rest_framework.serializers import ModelSerializer, CharField

from .models import condition_lvl

class ConditionSerializer(ModelSerializer):
    class Meta:
        model = condition_lvl
        fields = ['ConditionName']