from rest_framework.serializers import ModelSerializer

from apps.web.models import  EmploymentHistory


class EmploymentHistorySerializer(ModelSerializer):
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