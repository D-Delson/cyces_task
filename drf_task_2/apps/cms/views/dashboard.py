from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.cms.models import JobPost
from apps.common.models import User
from apps.common import ResponseUtils

class DashBoardAPIView(ResponseUtils,
                       APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        total_job_posts = JobPost.objects.count()
        total_applications = User.objects.count()

        counts = {
            'total_job_posts': total_job_posts,
            'total_applications': total_applications,
        }
        return Response(counts)
