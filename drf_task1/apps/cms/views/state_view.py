import csv

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.common.models import State
from apps.common.serializers import StateSerializer, StateCreateSerializer
from ..pagination import CustomPagination
from .response_utiles import handle_response

fs = FileSystemStorage(location='tmp/')

class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'state__name']

    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return StateCreateSerializer
        return StateSerializer

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

        state_list = []
        for id, row in enumerate(reader):
            (name, country_id) = row  
            state_list.append((name, country_id))
        State.objects.bulk_create([State(name=name, country_id = country_id) for name, country_id in state_list])
        return Response("Successfully uploaded the data!")

#view for csv export
class StateCSVExport(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

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
    