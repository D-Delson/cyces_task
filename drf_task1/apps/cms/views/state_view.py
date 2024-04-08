from rest_framework import viewsets

from apps.common.models import State
from apps.common.serializers import StateSerializer

class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer