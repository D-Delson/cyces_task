from rest_framework.serializers import ModelSerializer

from apps.web.models import WorkDetail, EmploymentHistory

class WorkDetailSerializer(ModelSerializer):
    class Meta:
        model = WorkDetail
        fields = '__all__'

class EmploymentHistory(ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'