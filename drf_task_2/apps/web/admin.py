from django.contrib import admin
from .models import Award, Certification, Education, \
                    Preference, WorkDetail, EmploymentHistory
# Register your models here.
admin.site.register(Award)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Preference)
admin.site.register(WorkDetail)
admin.site.register(EmploymentHistory)