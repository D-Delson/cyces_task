from rest_framework.serializers import ModelSerializer

from apps.common.models import User

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 2