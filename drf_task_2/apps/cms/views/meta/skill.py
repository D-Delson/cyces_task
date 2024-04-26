from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.cms.models import Skill
from apps.cms.serializers import Skillserializers

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = Skillserializers
    permission_classes = [IsAuthenticated]