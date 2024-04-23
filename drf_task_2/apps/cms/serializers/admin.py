from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.common.models import User
from apps.cms.models import Skill

class CombinedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone_number',
            'create_at',
            'work_detail'
        ]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        work_details = representation.pop('work_detail', [])
        serialized_work_details = []

        for work_detail in work_details:

            skill_id = work_detail['skill']
            skill_name = Skill.objects.get(id=skill_id).skill_name

            total_year_of_experience = work_detail['total_year_of_experiance']

            serialized_work_details.append({
                'skill_name': skill_name, 
                'total_year_of_experience': total_year_of_experience
                })
            
        representation['work_detail'] = serialized_work_details
        
        return representation
