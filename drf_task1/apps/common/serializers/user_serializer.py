from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import ValidationError

from ..models import UserProfile

from . import CountrySerializer, StateSerializer, CitySerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile

        fields = ['name', 'last_name', 'email', 'phone_number', 'country', 'state', 'city']

        validators = [
            UniqueTogetherValidator(
                queryset = UserProfile.objects.all(),
                fields = ['email', 'phone_number']
            )
        ]
    
    
    # def validate_phone_number(self, value):
    #     phone_number_list = [i for i in value]
    #     print(phone_number_list)
    #     if phone_number_list[0:3] == ['+', '9', '1']:
    #         if len(phone_number_list[3:]) != 10:
    #             raise ValidationError('Phone number should be 10 digits after country code!')
    #         elif len(phone_number_list[3:]) == 10:
    #             return value
    #     elif len(phone_number_list) != 10:
    #         raise ValidationError('Enter a valid 10-digit phone number')
    #     return value
            