from rest_framework import serializers

from ..models import City

from . import CountrySerializer, StateSerializer

class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()
    country = CountrySerializer()
    class Meta:
        model = City
        fields = ['name', 'state', 'country']