from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser

from apps.common.models import User
from apps.cms.serializers import CombinedSerializer
from apps.web.serializers import UserSerializers
from ..tasks import process_retrieve_action

class CMSViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CombinedSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name',
        'phone_number',
        'work_detail__skill__skill_name',
    ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializers
        return CombinedSerializer

    def retrieve(self, request, *args, **kwargs):
        process_retrieve_action.delay(kwargs['pk'])  
        return super().retrieve(request, *args, **kwargs)