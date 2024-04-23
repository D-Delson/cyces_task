from django.urls import path
from rest_framework import routers

from .views import CMSViewSet, JobPostViewSet, DashBoardAPIView, ChangePasswordAPIView

router  = routers.DefaultRouter()
router.register(r'users', CMSViewSet)
router.register(r'jobpost', JobPostViewSet)

urlpatterns = [
    path('dashboard/', DashBoardAPIView.as_view(), name='dashboard-view'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='password change' )
] + router.urls 

