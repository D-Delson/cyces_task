from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Skill
from apps.cms.serializers import Skillserializers
from apps.common import ResponseUtils

class SkillViewSet(ResponseUtils,
                   ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = Skillserializers
    permission_classes = [IsAuthenticated]