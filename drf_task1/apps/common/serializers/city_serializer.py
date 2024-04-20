from rest_framework import serializers

from ..models import City
from . import CountrySerializer, StateSerializer

class CitySerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'country']
    
    def get_state(self, obj):
        state = obj.state.name
        return state
    
    def get_country(self, obj):
        country = obj.country.name
        return country