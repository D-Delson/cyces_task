from rest_framework import serializers

from apps.common.models import User
from apps.cms.models import Country, State 

from apps.web.models import (
    Award,
    Certification, 
    Education,
    Preference,
    WorkDetail,
    EmploymentHistory
)

from .award  import AwardSerializers                        
from apps.web.serializers import CertificationSerializers
from apps.web.serializers import (
    EducationReadSerializers,
    EducationWriteSerializers
)
from .employment_history import (
    EmploymentHistoryReadSerializer,
    EmploymentHistoryWriteSerializer
)
from .preference import (
    PreferenceSerializers,
    PreferenceReadSerializer)
from .work_detail import (
    WorkDetailReadSerializer,
    WorkDetailWriteSerializer
)


class UserReadSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    education = EducationReadSerializers(many=True)
    certification = serializers.StringRelatedField(many=True)
    work_detail = WorkDetailReadSerializer(many=True)
    employment_history = EmploymentHistoryReadSerializer(many=True)
    awards = serializers.StringRelatedField(many=True)
    preference = PreferenceReadSerializer(many=True)

    def get_state(self, obj):
            return obj.state.state_name
        
    def get_country(self, obj):
        return obj.country.country_name
    class Meta:
        model = User
        fields = [
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

        
                                                      
                                
class UserWriteSerializers(serializers.ModelSerializer):
    education = EducationWriteSerializers(many=True)
    certification = CertificationSerializers(many=True)
    work_detail = WorkDetailWriteSerializer(many=True)
    employment_history = EmploymentHistoryWriteSerializer(many=True)
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
    
    def create(self, validate_data):

        state_id = validate_data.pop('state').id
        country_id = validate_data.pop('country').id
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
            degree_id = education["degree"]
            edu, _ = Education.objects.update_or_create(
                year_of_passing=education["year_of_passing"],
                school=education["school"],
                degree = degree_id
            )
            user.education.add(edu)
        
        for certificate in certification_data:
            cer, _ = Certification.objects.update_or_create(
                certification_name = certificate["certification_name"],
                certification_year = certificate["certification_year"]
            )
            user.certification.add(cer)

        for work in work_detail_data:
            work_data, _ = WorkDetail.objects.update_or_create(
                total_year_of_experiance = work["total_year_of_experiance"]
            )
            work_data.skill.add(*work['skill'])
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
            country_id = preference["country"]
            industry_id = preference["industries"]

            new_preference, _ = Preference.objects.update_or_create(
                country = country_id,
                industries=industry_id,
                position=preference["position"],
                available_from=preference["available_from"],
                salary_expectation=preference["salary_expectation"]

            )
            user.preference.add(new_preference)
        
        return user






