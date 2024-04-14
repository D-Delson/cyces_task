from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import City
from apps.common.serializers import CitySerializer, CityCreateSerializer
from ..pagination import CustomPagination
from  .response_utiles import handle_response

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'state__name', 'country__name']

    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CityCreateSerializer
        return CitySerializer

