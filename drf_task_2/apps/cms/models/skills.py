from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

class Skill(Base):
    skill_name = models.CharField(
        'Skill Name',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    def __str__(self):
        return self.skill_name