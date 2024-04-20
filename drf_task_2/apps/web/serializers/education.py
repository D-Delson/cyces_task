from rest_framework.serializers import ModelSerializer

from apps.web.models import Education

class EducationSerializers(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'