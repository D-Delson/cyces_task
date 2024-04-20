from django.db import models

from apps.common.models import Base
from apps.cms.models import Country, Industry

POSITION_CHOICES = [
    ('intern', 'Intern'),
    ('junior', 'Junior'),
    ('senior', 'Senior')
]

class Preference(Base):
    country = models.ForeignKey(
        Country,
        on_delete = models.CASCADE,
        default = 'India'
    )

    industries = models.ForeignKey(
        Industry,
        on_delete = models.CASCADE
    )

    position = models.CharField(
        'Position',
        choices = POSITION_CHOICES
    )

    available_from = models.DateField()

    salary_expectation = models.SmallIntegerField()

   

