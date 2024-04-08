from rest_framework import routers
from . views import UserRegistration

router = routers.SimpleRouter()
router.register(r'user', UserRegistration)

urlpatterns = router.urls
