from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)
from apps.common.models import User
from apps.cms.serializers import CombinedSerializer
from apps.web.serializers import UserReadSerializer
from apps.cms import process_retrieve_action 

class CMSViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name',
        'phone_number',
        'work_detail__skill__skill_name',
    ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserReadSerializer
        return CombinedSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        file_path = process_retrieve_action(user_id)#.delay(user_id).get()
        return Response({'file_path': file_path}, status=status.HTTP_200_OK)