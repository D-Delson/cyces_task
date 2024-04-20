from rest_framework.serializers import ModelSerializer

from apps.cms.models import Industry

class Industryserializers(ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'