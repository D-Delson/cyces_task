from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Country
from apps.cms.serializers import CountrySerializers

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    permission_classes = [IsAuthenticated]
