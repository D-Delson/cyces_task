from rest_framework.serializers import ModelSerializer

from apps.web.models import Certification

class CertificationSerializers(ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'