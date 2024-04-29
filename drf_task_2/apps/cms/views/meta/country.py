from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Country
from apps.cms.serializers import CountrySerializers
from apps.common import ResponseUtils


class CountryViewSet(ResponseUtils,
                     viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    permission_classes = [IsAuthenticated]

    
