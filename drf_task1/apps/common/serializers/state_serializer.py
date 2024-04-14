from rest_framework import serializers
from . import CountrySerializer
from ..models import State

class StateSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model = State
        fields = ['id', 'name', 'country']

    def get_country(self, obj):
        country = obj.country.name
        return country