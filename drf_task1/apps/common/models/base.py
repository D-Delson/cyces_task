from django.db import models
from django.core.validators import RegexValidator

class Base(models.Model):
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        abstract = True


def name_validator(value):
    return RegexValidator(regex='^[A-Za-z]*$', message='only a-z')(value)




