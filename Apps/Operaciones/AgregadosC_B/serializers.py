from rest_framework.serializers import ModelSerializer, CharField

from .models import aggregates_cb

class AggregatesCbSerializer(ModelSerializer):
    comida = CharField(source='foodFK.foodName', label='Comidas', read_only=True)
    bebida = CharField(source='beverageFK.NameBeverage', label='Bebida', read_only=True)

    class Meta:
        model = aggregates_cb
        fields = ['idAggregates', 'codeAggregates', 'foodFK', 'comida', 'beverageFK', 'bebida']

class AgreggatesWriteSerializer(ModelSerializer):
    class Meta:
        model = aggregates_cb
        fields = ['idAggregates', 'codeAggregates', 'foodFK', 'beverageFK']

class AgreggatesLookupSerializer(ModelSerializer):
    class Meta:
        model = aggregates_cb
        fields = ['idAggregates', 'codeAggregates']