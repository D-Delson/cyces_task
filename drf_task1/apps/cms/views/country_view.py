from rest_framework import viewsets, filters, status
from rest_framework.response import Response


from apps.common.models import Country
from apps.common.serializers import CountrySerializer
from ..pagination  import CustomPagination

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)

   
