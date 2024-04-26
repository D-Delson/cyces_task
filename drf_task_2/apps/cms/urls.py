from django.urls import path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    ApplicationView,
    ChangePasswordAPIView,
    CountryViewSet,
    CMSViewSet,
    DashBoardAPIView,
    DegreeViewSet,
    IndustryViewSet,
    JobPostViewSet,
    StateModelViewSet,
    SkillViewSet
)
   
router  = routers.DefaultRouter()
router.register(r'users', CMSViewSet)
router.register(r'jobpost', JobPostViewSet)
router.register(r'country', CountryViewSet)
router.register(r'state', StateModelViewSet)
router.register(r'degree', DegreeViewSet)
router.register(r'industry', IndustryViewSet)
router.register(r'skill', SkillViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/', DashBoardAPIView.as_view(), name='dashboard-view'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='password change' ),
    path('users/<int:pk>/', ApplicationView.as_view(), name='application_view')
] + router.urls 