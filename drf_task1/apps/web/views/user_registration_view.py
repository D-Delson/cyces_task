from django.core.mail import send_mail
from rest_framework import mixins
from rest_framework import viewsets

from apps.common.models import UserProfile
from apps.common.serializers import UserSerializer 
from apps.cms.views.response_utiles import handle_response

class UserRegistration(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

