from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/web/', include('apps.web.urls')),
    path('api/cms/', include('apps.cms.urls'))
]
