from rest_framework import viewsets

from apps.common.models import Country
from apps.common.serializers import CountrySerializer

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer