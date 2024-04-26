from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

from .country import Country

class State(Base):
    state_name = models.CharField(
        'State Name',
        max_length = MAX_LENGTH,
        validators = [validate_name],
        unique=True
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='state'
    )