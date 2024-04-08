from rest_framework import serializers
from ..models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'last_name', 'email', 'phone_number', 'country', 'state', 'city']