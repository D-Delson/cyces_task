from rest_framework import viewsets
from apps.common.models import City
from apps.common.serializers import CitySerializer

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer