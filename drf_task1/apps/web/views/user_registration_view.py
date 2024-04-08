from rest_framework import mixins
from rest_framework import viewsets

from apps.common.models import UserProfile
from apps.common.serializers import UserSerializer 

class UserRegistration(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
                    