from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.web.models import  EmploymentHistory


class EmploymentHistoryReadSerializer(ModelSerializer):
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    class Meta:
        model = EmploymentHistory
        fields = [
            'job_title',
            'employer',
            'city',
            'state',
            'country'
        ]
    def get_state(self, obj):
        return obj.state.state_name

    def get_country(self, obj):
        return obj.country.country_name

class EmploymentHistoryWriteSerializer(ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = [
            'id',
            'job_title',
            'employer',
            'city',
            'state',
            'country'
        ]