from django.core.validators import EmailValidator, RegexValidator
from django.db import models

from . import Base
from . import name_validator
from ..constants import MAX_LENGTH


class UserProfile(Base):
    name = models.CharField(
        'first name',
        max_length = MAX_LENGTH,
        validators = [name_validator],
    )

    last_name = models.CharField(
        'last name',
        max_length = MAX_LENGTH,
        validators = [name_validator],
    )

    email = models.EmailField(
        'Email',
        unique = True,
        validators = [EmailValidator()]
    )

    phone_number = models.CharField(
        'phone number',
        max_length = MAX_LENGTH,
        unique = True,
        validators = [RegexValidator(regex='^(\d){10}$', message='only numbers 0-9')]
    )

    country = models.ForeignKey(
        'Country',
        on_delete = models.CASCADE
    )

    state = models.ForeignKey(
        'State',
        on_delete = models.CASCADE,
    )

    city = models.ForeignKey(
        'City',
        on_delete = models.CASCADE
    )

    is_admin = False

    def __str__(self):
        return self.name



