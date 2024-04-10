from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import State
from apps.common.serializers import StateSerializer

class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country__name']