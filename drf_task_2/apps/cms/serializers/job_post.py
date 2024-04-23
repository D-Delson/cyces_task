from rest_framework.serializers import ModelSerializer

from apps.cms.models import JobPost

class JobPostSerializer(ModelSerializer):
    class Meta:
        model = JobPost
        fields = [
            'id',
            'job_name',
            'skill',
            'industry',
            'vacancies',
            'posted_on',
        ]
        depth = 1