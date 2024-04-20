from rest_framework.serializers import ModelSerializer

from apps.cms.models import Skill

class Skillserializers(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'