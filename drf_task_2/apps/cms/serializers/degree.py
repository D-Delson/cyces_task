from rest_framework.serializers import ModelSerializer

from apps.cms.models import Degree

class DegreeSerializers(ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'