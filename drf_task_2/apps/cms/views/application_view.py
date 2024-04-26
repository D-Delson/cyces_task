from rest_framework import generics
from apps.common.models import User
from apps.web.serializers import UserReadSerializer

class ApplicationView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer