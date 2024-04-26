from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.web.models import Preference

class PreferenceReadSerializer(ModelSerializer):
    country = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    class Meta:
        model = Preference
        fields = [
            'country',
            'industries',
            'position',
            'available_from',
            'salary_expectation'
        ]
    def get_country(self, obj):
        return obj.country.country_name
    def get_industries(self, obj):
        return obj.industries.industry_name

class PreferenceSerializers(ModelSerializer):
    class Meta:
        model = Preference
        fields = [
            'id',
            'country',
            'industries',
            'position',
            'available_from',
            'salary_expectation'
        ]