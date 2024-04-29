from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Industry
from apps.cms.serializers import Industryserializers
from apps.common import ResponseUtils

class IndustryViewSet(ResponseUtils,
                      ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = Industryserializers
    permission_classes = [IsAuthenticated]