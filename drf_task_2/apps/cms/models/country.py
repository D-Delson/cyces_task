from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

class Country(Base):
    country_name = models.CharField(
        'Country Name',
        max_length = MAX_LENGTH,
        validators = [validate_name],
        default = 'India',
        unique=True
    )