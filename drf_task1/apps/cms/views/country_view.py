from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import Country
from apps.common.serializers import CountrySerializer
from ..pagination  import CustomPagination

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

   
