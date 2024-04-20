from rest_framework.serializers import ModelSerializer

from apps.web.models import Preference

class PreferenceSerializers(ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'