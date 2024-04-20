from django.urls import path
from rest_framework import routers

from .views import UserListView, CountryView,  CityView, StateView, UserCSVExport, \
                   CountryCSVExport, StateCSVExport, CityCSVExport

router = routers.SimpleRouter()
router.register(r'user_list', UserListView)
router.register(r'country', CountryView)
router.register(r'state', StateView)
router.register(r'city', CityView)

EXPORT_PATH = 'export/csv'

urlpatterns = [
    path(f'user_list/{EXPORT_PATH}', UserCSVExport.as_view(), name='user_csv_export'),
    path(f'country/{EXPORT_PATH}', CountryCSVExport.as_view(), name='country_csv_export'),
    path(f'state/{EXPORT_PATH}', StateCSVExport.as_view(), name='state_csv_export'),
    path(f'city/{EXPORT_PATH}', CityCSVExport.as_view(), name='city_csv_export')
]
urlpatterns = router.urls + urlpatterns




