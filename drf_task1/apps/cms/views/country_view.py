import csv

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.common.models import Country
from apps.common.serializers import CountrySerializer
from ..pagination  import CustomPagination
from .response_utiles import handle_response

fs = FileSystemStorage(location='tmp/')

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    #for create
    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    #for update
    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
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

        country_list = []
        for id, row in enumerate(reader):
            (name,) = row  
            country_list.append(name)
        Country.objects.bulk_create([Country(name=name) for name in country_list])
        return Response("Successfully uploaded the data!")

#export csv file data
class CountryCSVExport(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

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


   
