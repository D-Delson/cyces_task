from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.web.models import WorkDetail

class WorkDetailReadSerializer(ModelSerializer):
    skill = serializers.StringRelatedField(many=True)
    class Meta:
        model = WorkDetail
        fields = [
            'skill',
            'total_year_of_experiance'
        ]

class WorkDetailWriteSerializer(ModelSerializer):
    class Meta:
        model = WorkDetail
        fields = [
            'skill',
            'total_year_of_experiance'
        ]

