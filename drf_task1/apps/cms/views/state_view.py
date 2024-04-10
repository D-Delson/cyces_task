from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import State
from apps.common.serializers import StateSerializer
from ..pagination import CustomPagination

class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country__name']