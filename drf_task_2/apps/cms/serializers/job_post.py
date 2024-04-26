from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.cms.models import JobPost


class JobPostReadSerializer(ModelSerializer):
    skill = serializers.StringRelatedField(many=True)
    industry = serializers.SerializerMethodField()
    class Meta:
        model = JobPost
        fields = [
            'id',
            'job_name',
            'skill',
            'industry',
            'vacancies',
            'posted_on'
        ]
    def get_industry(self, obj):
        return obj.industry.industry_name

class JobPostWriteSerializer(ModelSerializer):
    class Meta:
        model = JobPost
        fields = [
            'job_name',
            'skill',
            'industry',
            'vacancies',
        ]