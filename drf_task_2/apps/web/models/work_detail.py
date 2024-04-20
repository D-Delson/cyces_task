from django.db import models

from apps.common.models import Base, validate_name
from apps.cms.models import Skill, State, Country
from apps.common import MAX_LENGTH


WORKING_EXP = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10+'),
]

class WorkDetail(Base):


    skill = models.ForeignKey(
        Skill,
        on_delete = models.CASCADE
    )

    total_year_of_experiance = models.IntegerField(
        choices = WORKING_EXP
    )


class EmploymentHistory(Base):
    job_title = models.CharField(
        'Job Title',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    employer = models.CharField(
        'Employer',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    city = models.CharField(
        'City',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    state = models.ForeignKey(
        State,
        on_delete = models.CASCADE
    )

    country = models.ForeignKey(
         Country,
         on_delete =  models.CASCADE
    )

    def __str__(self) -> str:
        return self.job_title