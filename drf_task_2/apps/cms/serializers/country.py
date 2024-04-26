from rest_framework.serializers import ModelSerializer

from apps.cms.models import Country

class CountrySerializers(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'country_name'
            ]