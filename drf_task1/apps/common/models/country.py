from django.db import models

from . import Base
from . import name_validator
from ..constants import MAX_LENGTH

class Country(Base):
    name = models.CharField(
        'country name',
        max_length = MAX_LENGTH,
        validators = [name_validator],
    )

    def __str__(self):
        return self.name