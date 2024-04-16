import csv
import os
import pytz
from datetime import datetime
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.views.generic import View

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAdminUser

from config import settings
from apps.common.models import UserProfile, City, State, Country
from apps.common.serializers import UserListSerializer
from ..pagination import CustomPagination

class UserListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'last_name', 'city__name', 'state__name', \
                     'country__name', 'phone_number', 'email']


class UserCSVExport(View):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        print(serializer)

        csv_data = [serializer.data[0].keys()]  
        csv_data += [item.values() for item in serializer.data]

        model_name = self.serializer_class.Meta.model.__name__.lower()
        current_datetime = datetime.now(pytz.timezone('UTC')).strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{model_name}_data_{current_datetime}.csv"

        file_path = os.path.join(settings.BASE_DIR, filename)
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
        response_data = {
            'filename': filename
        }
        return JsonResponse(response_data)
    