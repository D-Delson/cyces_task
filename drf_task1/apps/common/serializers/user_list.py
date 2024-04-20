from rest_framework import serializers
from ..models import UserProfile

class UserListSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['id','name', 'last_name', 'email', 'phone_number', \
                  'country', 'state', 'city']
    
    def get_country(self, obj):
        country = obj.country.name
        return country

    def get_state(self, obj):
        state = obj.state.name
        return state
    
    def get_city(self, obj):
        city = obj.city.name
        return city
    

            