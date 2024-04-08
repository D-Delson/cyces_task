from rest_framework import viewsets, mixins

from apps.common.models import UserProfile
from apps.common.serializers import UserSerializer

class UserListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer