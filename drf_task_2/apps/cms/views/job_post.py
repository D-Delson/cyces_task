from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.cms.models import JobPost, Skill, Industry
from apps.cms.serializers import JobPostSerializer


class JobPostViewSet(ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        
        #adding industry
        industry_name = data['industry']['industry_name']
        industry_id, _ = Industry.objects.update_or_create(industry_name=industry_name)

        job_post = JobPost.objects.create(
            job_name=data['job_name'],
            vacancies=data['vacancies'],
            industry=industry_id,
        )

        job_post.save()
        # adding skill
        for skill in data['skill']:
            skill_id, _ = Skill.objects.update_or_create(skill_name=skill)
            job_post.skill.add(skill_id) 

        serializer = JobPostSerializer(job_post)
        return Response(serializer.data)

        


