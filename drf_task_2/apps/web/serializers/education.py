from rest_framework.serializers import ModelSerializer

from apps.web.models import Education
from apps.cms.serializers import DegreeSerializers

class EducationSerializers(ModelSerializer):
    degree = DegreeSerializers()
    class Meta:
        model = Education
        fields = [
            'id',
            'degree',
            'year_of_passing',
            'school'
        ]