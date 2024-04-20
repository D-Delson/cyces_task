from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

class State(Base):
    state_name = models.CharField(
        'State Name',
        max_length = MAX_LENGTH,
        validators = [validate_name],
        unique=True
    )