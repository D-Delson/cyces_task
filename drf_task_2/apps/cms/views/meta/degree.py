from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Degree
from apps.cms.serializers import DegreeSerializers

class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializers
    permission_classes = [IsAuthenticated]