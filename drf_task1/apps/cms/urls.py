from rest_framework import routers

from .views import UserListView, CountryView, StateView, CityView

router = routers.SimpleRouter()


router.register(r'user_list', UserListView)
router.register(r'country', CountryView)
router.register(r'state', StateView)
router.register(r'city', CityView)
urlpatterns = router.urls

