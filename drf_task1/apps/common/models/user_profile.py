from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from rest_framework import filters

from phonenumber_field.modelfields import PhoneNumberField

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
    )

    phone_number = PhoneNumberField()

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



