from rest_framework import viewsets, mixins
from rest_framework import filters

from apps.common.models import UserProfile
from apps.common.serializers import UserSerializer
from ..pagination import CustomPagination

class UserListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'last_name', 'city__name', 'state__name', 'country__name']