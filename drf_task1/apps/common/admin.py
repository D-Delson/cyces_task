from django.contrib import admin

from .models import Country, City, State, UserProfile

admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(UserProfile)