from rest_framework import serializers
from ..models import City

class CityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'country']
    