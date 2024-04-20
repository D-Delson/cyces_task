from django.db import models
from . import Base
from . import name_validator
from ..constants import MAX_LENGTH


class City(Base):
    name = models.CharField(
        'city name',
        max_length = MAX_LENGTH,
        validators = [name_validator],
        unique=True
    )

    state = models.ForeignKey(
        'State',
        on_delete=models.CASCADE
    )

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name