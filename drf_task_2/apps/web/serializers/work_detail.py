from rest_framework.serializers import ModelSerializer

from apps.web.models import WorkDetail

class WorkDetailSerializer(ModelSerializer):

    class Meta:
        model = WorkDetail
        fields = [
            'skill',
            'total_year_of_experiance'
        ]

