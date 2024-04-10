from rest_framework import serializers
from . import CountrySerializer
from ..models import State

class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = State
        fields = ['name', 'country']