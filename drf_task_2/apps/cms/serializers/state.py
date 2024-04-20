from rest_framework.serializers import ModelSerializer

from apps.cms.models import State

class StateSerializers(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'