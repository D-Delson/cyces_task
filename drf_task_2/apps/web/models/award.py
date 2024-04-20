from django.db import models
from apps.common.models  import Base, validate_name

from apps.common import MAX_LENGTH

class Award(Base):
    award_name = models.CharField(
        'Award Name',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    organisation = models.CharField(
        'Awarding Organization',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    def __str__(self):
        return self.award_name