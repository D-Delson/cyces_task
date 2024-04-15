import csv

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView

from apps.common.models import City
from apps.common.serializers import CitySerializer, CityCreateSerializer
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
        csv_file = open(tmp_file, errors='ignore')
        reader = csv.reader(csv_file)
        next(reader)

        city_list = []
        for id, row in enumerate(reader):
            (name, state_id, country_id) = row  
            city_list.append((name,state_id, country_id))
        City.objects.bulk_create([City( name = name,                       \
                                         state_id = state_id,               \
                                         country_id = country_id)            \
                                         for name, state_id, country_id in city_list])
        return Response("Successfully uploaded the data!")

class CityCSVExport(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="yourmodel_data.csv"'

        writer = csv.writer(response)
        writer.writerow(serializer.data[0].keys())  
        for item in serializer.data:
            writer.writerow(item.values())

        return response

