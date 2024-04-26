from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.web.models import Education

class EducationReadSerializers(ModelSerializer):
    degree = serializers.SerializerMethodField()
    class Meta:
        model = Education
        fields = [
            'id',
            'degree',
            'year_of_passing',
            'school'
        ]
    
    def get_degree(self, obj):
        return obj.degree.degree_name
    
class EducationWriteSerializers(ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'degree',
            'year_of_passing',
            'school'
        ]