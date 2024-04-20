from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

class Certification(Base):
    certification_name = models.CharField(
        'certification_name',
        max_length = MAX_LENGTH,
        validators = [ validate_name ]
    )

    certification_year = models.IntegerField(
        'year of certification',
        validators = [
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )

    def __str__(self):
        return self.certification_name