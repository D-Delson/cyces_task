from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.common.models import User
from apps.cms.models import Skill
from apps.web.models import WorkDetail

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
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        serialized_work_details = []
        for work_detail_id in representation['work_detail']:
            work_detail_obj = WorkDetail.objects.get(id=work_detail_id)
            skills = work_detail_obj.skill.all()
            serialized_skills = []
            for skill in skills:
                serialized_skills.append({
                    'skill_name': skill.skill_name,
                    'total_year_of_experience': work_detail_obj.total_year_of_experiance
                })
            serialized_work_details.extend(serialized_skills)

        representation['work_detail'] = serialized_work_details
        return representation
