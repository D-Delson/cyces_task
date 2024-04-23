# views.py
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cms.models import JobPost
from apps.cms.serializers import DashBoardSerializer
from apps.common.models import User

class DashBoardAPIView(APIView):
    def get(self, request):
        total_job_posts = JobPost.objects.count()
        total_applications = User.objects.count()

        counts = {
            'total_job_posts': total_job_posts,
            'total_applications': total_applications,
        }

        serializer = DashBoardSerializer(counts)
        return Response(serializer.data)
