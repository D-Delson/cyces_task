from rest_framework import viewsets
from rest_framework import filters

from apps.common.models import Country
from apps.common.serializers import CountrySerializer

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        print('destroys works')
        instance = self.get_object()
        instance.is_active = False
        return Response(status=status.HTTP_204_NO_CONTENT)

