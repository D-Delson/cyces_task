from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH
from apps.cms.models import Skill, Industry

class JobPost(Base):
    job_name = models.CharField(
        'Job Name',
        max_length=MAX_LENGTH,
        validators=[validate_name],
        null=False,
        blank=False
    )

    skill = models.ManyToManyField(
        Skill 
    )

    industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE
    )

    vacancies = models.SmallIntegerField()

    posted_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.job_name