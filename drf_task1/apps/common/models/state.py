from django.db import models

from . import Base
from . import name_validator
from ..constants import MAX_LENGTH

class State(Base):
    name = models.CharField(
        'state name',
        max_length = MAX_LENGTH,
        unique = True,
        validators = [name_validator],
    )

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name