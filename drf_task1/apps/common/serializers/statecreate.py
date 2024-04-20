from rest_framework import serializers
from ..models import State

class StateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'country']
