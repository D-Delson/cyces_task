from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from apps.common.models import User
from apps.cms.serializers import CombinedSerializer
from apps.web.serializers import UserSerializers
from apps.cms import process_retrieve_action 

class CMSViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
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
        user_id = kwargs['pk']
        file_path = process_retrieve_action.delay(user_id).get()
        return Response({'file_path': file_path}, status=status.HTTP_200_OK)