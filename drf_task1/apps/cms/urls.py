from django.urls import path
from rest_framework import routers

from .views import UserListView, CountryView,  CityView, StateView, UserCSVExport, \
                   CountryCSVExport, StateCSVExport, CityCSVExport

router = routers.SimpleRouter()
router.register(r'user_list', UserListView)
router.register(r'country', CountryView)
router.register(r'state', StateView)
router.register(r'city', CityView)

urlpatterns = [
    path('user_list/export/csv', UserCSVExport.as_view(), name='user_csv_export'),
    path('country/export/csv', CountryCSVExport.as_view(), name='country_csv_export'),
    path('state/export/csv', StateCSVExport.as_view(), name='state_csv_export'),
    path('city/export/csv', CityCSVExport.as_view(), name='city_csv_export')
]
urlpatterns = router.urls + urlpatterns




