import csv
import os
import pytz

from datetime import datetime
from django.http import JsonResponse
from django.views.generic import View
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters

from apps.common.models import City, State, Country
from apps.common.serializers import CitySerializer, CityCreateSerializer
from config import settings
from ..pagination import CustomPagination
from  .response_utiles import handle_response

fs = FileSystemStorage(location='tmp/')

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'state__name', 'country__name']

    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CityCreateSerializer
        return CitySerializer

    #import csv file data
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES["file"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save("_tem.csv", file_content)
        tmp_file = fs.path(file_name)

        with open(tmp_file, errors='ignore') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for id, row in enumerate(reader):
                name = row[0].strip().lower()
                state_name = row[1].strip().lower()
                country_name = row[2].strip().lower()

                state = State.objects.get(name=state_name)
                country = Country.objects.get(name=country_name)

                city, _ = City.objects.update_or_create(
                    name__iexact = name,
                    state = state,
                    country = country,
                    defaults = {
                        "name" : name
                    }
                )
        return Response("Successfully uploaded the data!")

   

class CityCSVExport(View):
    queryset = City.objects.all()
    serializer_class = CitySerializer

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

