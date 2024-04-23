from rest_framework.serializers import ModelSerializer

from apps.web.models import Award

class AwardSerializers(ModelSerializer):
    class Meta:
        model = Award
        fields = [
            'id',
            'award_name',
            'organisation']