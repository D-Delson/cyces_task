from django.db import models

from apps.common.models import Base
from apps.common import MAX_LENGTH

class Degree(Base):
    degree_name = models.CharField(
        'Degree name',
        max_length = MAX_LENGTH
    )

    def __str__(self):
        return self.degree_name


