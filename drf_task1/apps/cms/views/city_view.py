from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import City
from apps.common.serializers import CitySerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']