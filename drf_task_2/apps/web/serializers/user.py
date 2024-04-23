from rest_framework.serializers import ModelSerializer

from apps.common.models import User
from apps.cms.serializers import StateSerializers, CountrySerializers
from apps.web.serializers import CertificationSerializers,\
                                 EducationSerializers \
                                 


class UserSerializers(ModelSerializer):
    state = StateSerializers()
    country = CountrySerializers()
    education = EducationSerializers(many=True)
    certification = CertificationSerializers(many=True)
    
    class Meta: 
        model = User
        # fields = '__all__'
        exclude = [
            'create_at',
            'updated_at',
            'is_active'
        ]
        depth = 2
        unique_together = [('email', 'phone_number')]



