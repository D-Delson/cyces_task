from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.common.models import Base, validate_name
from apps.cms.models import Degree

from apps.common import MAX_LENGTH

class Education(Base):
    degree = models.ForeignKey(
        Degree,
        on_delete = models.CASCADE
    )

    year_of_passing = models.IntegerField(
        'passing year',
         validators = [
             MinValueValidator(1000),
             MaxValueValidator(9999)
         ]
    )

    school = models.CharField(
        'school',
         max_length = MAX_LENGTH,
         validators = [validate_name]

    )
