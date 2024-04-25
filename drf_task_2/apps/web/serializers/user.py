from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.common.models import User
from apps.cms.models import Country,Degree,Industry,Skill, State 
from apps.cms.serializers import StateSerializers

from apps.web.models import Award
from apps.web.models import Certification
from apps.web.models import Education
from apps.web.models import Preference
from apps.web.models import WorkDetail
from apps.web.models import EmploymentHistory 

from .award  import AwardSerializers                        
from apps.web.serializers import CertificationSerializers
from apps.web.serializers import EducationSerializers

from .employment_history import EmploymentHistorySerializer
from .preference import PreferenceSerializers
from .work_detail import WorkDetailSerializer
                       
                                 
                                
class UserSerializers(ModelSerializer):
    
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), source='state_id')
    country  = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), source='country_id')

    education = EducationSerializers(many=True)
    certification = CertificationSerializers(many=True)
    work_detail = WorkDetailSerializer(many=True)
    employment_history = EmploymentHistorySerializer(many=True)
    awards = AwardSerializers(many=True)
    preference = PreferenceSerializers(many=True)

    class Meta: 
        model = User
        fields = [
            'id',
            'name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'city',
            'pincode',
            'state',
            'country',
            'education',
            'certification',
            'work_detail',
            'employment_history',
            'awards',
            'preference',
        ]
        depth = 2
        unique_together = [('email', 'phone_number')]
    
    def create(self, validate_data):

        state_id = validate_data.pop('state_id').id
        country_id = validate_data.pop('country_id').id
        state = State.objects.get(id=state_id)
        country = Country.objects.get(id=country_id)
        
        education_data = validate_data.pop('education')
        certification_data = validate_data.pop('certification')
        work_detail_data = validate_data.pop('work_detail')
        employment_history_data = validate_data.pop('employment_history')
        awards_data = validate_data.pop('awards')
        preference_data = validate_data.pop('preference')


        user = User.objects.create(state=state, country=country, **validate_data)
        user.save()

        for education in education_data:
            degree_name = education["degree"]["degree_name"]
            degree_id, _ = Degree.objects.update_or_create(degree_name = degree_name)

            edu, _ = Education.objects.update_or_create(
                year_of_passing=education["year_of_passing"],
                school=education["school"],
                degree = degree_id
            )
            user.education.add(edu)
        
        for certificate in certification_data:
            cer, _ = Certification.objects.get_or_create(
                certification_name = certificate["certification_name"],
                certification_year = certificate["certification_year"]
            )
            user.certification.add(cer)

        for work in work_detail_data:

            work_data, _ = WorkDetail.objects.get_or_create(
                skill = work['skill'], 
                total_year_of_experiance = work["total_year_of_experiance"]
            )

            user.work_detail.add(work_data)

        for history in employment_history_data:
            new_emp_history, _ = EmploymentHistory.objects.get_or_create(
                    job_title=history["job_title"],
                    employer=history["employer"],
                    city=history["city"],
                    state=history['state'],
                    country=history['country']
            )
            user.employment_history.add(new_emp_history)
        
        for award in awards_data:
            new_award, _ = Award.objects.update_or_create(
                award_name=award["award_name"],
                organisation=award["organisation"]
            )
            user.awards.add(new_award)

        for preference in preference_data:
            country_name = preference["country"].id
            country_id, _ = Country.objects.update_or_create(country_name=country_name)

            industry_name = preference["industries"].id
            industry_id, _ = Industry.objects.update_or_create(industry_name=industry_name)

            new_preference, _ = Preference.objects.update_or_create(
                country = country_id,
                industries=industry_id,
                position=preference["position"],
                available_from=preference["available_from"],
                salary_expectation=preference["salary_expectation"]

            )
            user.preference.add(new_preference)
        
        return user






