from django.db import models

from apps.common.models import Base, validate_name
from apps.common import MAX_LENGTH

class Industry(Base):
    industry_name = models.CharField(
        'Industry_Name',
        max_length = MAX_LENGTH,
        validators = [validate_name]
    )

    def __str__(self):
        return self.industry_name
    
    
