from django.contrib import admin

from .models import Country, Degree, Industry, Skill, State, JobPost


admin.site.register(Country)
admin.site.register(Degree)
admin.site.register(Industry)
admin.site.register(Skill)
admin.site.register(State)
admin.site.register(JobPost)
