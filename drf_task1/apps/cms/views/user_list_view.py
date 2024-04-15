import csv
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from apps.common.models import UserProfile
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


class UserCSVExport(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializer

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
    
    # #import csv file data
    # @action(detail=False, methods=['POST'])
    # def upload_data(self, request):
    #     file = request.FILES["file"]
    #     content = file.read()
    #     file_content = ContentFile(content)
    #     file_name = fs.save("_tem.csv", file_content)
    #     tmp_file = fs.path(file_name)
    #     csv_file = open(tmp_file, errors='ignore')
    #     reader = csv.reader(csv_file)
    #     next(reader)

    #     user_list = []
    #     for id, row in enumerate(reader):
    #         (name, last_name, email, phone_number, city_id, state_id, country_id) = row  
    #         user_list.append((name,
    #                           last_name,
    #                           email,
    #                           phone_number,
    #                           city_id,
    #                           state_id, 
    #                           country_id))
    #     UserProfile.objects.bulk_create([UserProfile( name = name,   
    #                                                   last_name = last_name,
    #                                                   email = email,
    #                                                   phone_number = phone_number,
    #                                                   city_id = city_id,                    
    #                                                   state_id = state_id,               
    #                                                   country_id = country_id)            
    #                                      for name, state_id, country_id in city_list])
    #     return Response("Successfully uploaded the data!")