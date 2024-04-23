from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import viewsets

from ..serializers import UserSerializers
#import models
from apps.common.models import User
from apps.cms.models import State, Country, Degree, Skill, Industry
from apps.web.models import Education, Certification,WorkDetail, EmploymentHistory, Award, \
                            Preference

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    def create(self, request, *args, **kwargs):
        data = request.data

        #adding state
        state_name = data["state"]["state_name"]
        state, _ = State.objects.update_or_create(state_name=state_name)

        #adding country
        country_name = data["country"]["country_name"]
        country, _ = Country.objects.update_or_create(country_name=country_name)

        user = User.objects.create(
            name=data["name"],
            last_name=data["last_name"],
            phone_number=data["phone_number"],
            email=data["email"],
            address=data["address"],
            city=data["city"],
            pincode=data["pincode"],
            state=state,
            country=country,
        )
        user.save()

        #adding Many to Many Fields

        #adding Education
        for edu in data["education"]:
            #getting degree
            degree = edu["degree"]["degree_name"]
            degree_id, _ = Degree.objects.get_or_create(degree_name=degree)

            education, _ = Education.objects.get_or_create(
                year_of_passing=edu["year_of_passing"],
                school=edu["school"],
                degree = degree_id
            )
            user.education.add(education)

        #adding certificate
        for certificate in data["certification"]:
            cer, _ = Certification.objects.get_or_create(
                certification_name = certificate["certification_name"],
                certification_year = certificate["certification_year"]
            )
            user.certification.add(cer)

        #adding work details
        for work in data["work_detail"]:

            skill_name = work["skill"]["skill_name"]
            skill_id, _ = Skill.objects.update_or_create(skill_name=skill_name)

            work_data, _ = WorkDetail.objects.get_or_create(
                skill = skill_id, 
                total_year_of_experiance = work["total_year_of_experiance"]
            )

            user.work_detail.add(work_data)

        #employment history
        for history in data["employment_history"]:

            state_name = history["state"]["state_name"]
            state_id, _ = State.objects.update_or_create(state_name=state_name)

            country_name = history["country"]["country_name"]
            country_id, _ = Country.objects.update_or_create(country_name=country_name)
            new_emp_history, _ = EmploymentHistory.objects.get_or_create(
                    job_title=history["job_title"],
                    employer=history["employer"],
                    city=history["city"],
                    state=state_id,
                    country=country_id
            )
            user.employment_history.add(new_emp_history)

        #adding awards
        for award in data["awards"]:
            new_award, _ = Award.objects.update_or_create(
                award_name=award["award_name"],
                organisation=award["organisation"]
            )
            user.awards.add(new_award)

        #adding preference
        for preference in data["preference"]:
            country_name = preference["country"]["country_name"]
            country_id, _ = Country.objects.update_or_create(country_name=country_name)

            industry_name = preference["industries"]["industry_name"]
            industry_id, _ = Industry.objects.update_or_create(industry_name=industry_name)

            new_preference, _ = Preference.objects.update_or_create(
                country = country_id,
                industries=industry_id,
                position=preference["position"],
                available_from=preference["available_from"],
                salary_expectation=preference["salary_expectation"]

            )
            user.preference.add(new_preference)



        serializer = UserSerializers(user)
        return Response(serializer.data)
        

        


        