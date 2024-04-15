from django.core.mail import send_mail
from rest_framework import mixins
from rest_framework import viewsets

from apps.common.models import UserProfile
from apps.common.serializers import UserSerializer 
from config import settings

class UserRegistration(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
                    
    def perform_create(self, serializer):
        instance = serializer.save()
        subject = 'Welcome to our website'
        message = f'Hello {instance.name}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)