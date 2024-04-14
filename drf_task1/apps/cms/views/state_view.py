from rest_framework import viewsets, filters

from apps.common.models import State
from apps.common.serializers import StateSerializer, StateCreateSerializer
from ..pagination import CustomPagination
from .response_utiles import handle_response


class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country__name']

    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return StateCreateSerializer
        return StateSerializer
