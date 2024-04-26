from rest_framework import serializers

from apps.cms.models import State


class StateReadSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model = State
        fields = ['id', 'state_name', 'country']
    
    def get_country(self, obj):
        return obj.country.country_name

class StateWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name', 'country']