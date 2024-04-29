from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import State
from apps.common import ResponseUtils
from apps.cms.serializers import (
    StateReadSerializer,
    StateWriteSerializer
)


class StateModelViewSet(ResponseUtils,
                        ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return StateWriteSerializer
        return StateReadSerializer
