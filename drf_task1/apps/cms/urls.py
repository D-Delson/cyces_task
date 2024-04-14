from django.urls import path
from rest_framework import routers

from .views import UserListView, CountryView,  CityView, StateView

router = routers.SimpleRouter()
router.register(r'user_list', UserListView)
router.register(r'country', CountryView)
router.register(r'state', StateView)
router.register(r'city', CityView)

# urlpatterns = [
#     path('state/create', StateCreateAPIView.as_view(), name='create state'),
#     path('state/list/', StateListRetriveDestroyAPIView.as_view(), name='state list'),
#     path('state/update/<int:pk>/', StateUpdateAPIView.as_view(), name='update state'),
#     #path('state/<int:pk>/', StateListRetriveDestroyAPIView.as_view(), name='state retrive'),
#     path('state/delete/<int:pk>/', StateListRetriveDestroyAPIView.as_view(), name='delete state')
# ]

urlpatterns = router.urls


