from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.cms.models import State, Country
from apps.web.models import (
    Education,
    Certification,
    Award,
    Preference,
    WorkDetail,
    EmploymentHistory
)

from . import Base
from . import validate_name, validate_pincode
from .. import MAX_LENGTH

class User(Base):
    name = models.CharField(
        'First Name',
        max_length = MAX_LENGTH, 
        validators = [validate_name]
    )

    last_name = models.CharField(
        'Last Name',
        max_length = MAX_LENGTH, 
        validators = [validate_name]
    )

    phone_number = PhoneNumberField(
        verbose_name = 'Phone Number',
        region = 'IN',
    )

    email = models.EmailField(
        'Email',
        unique=True
    )

    address = models.TextField(
        'Address',
    )

    city = models.CharField(
        'City',
        max_length = MAX_LENGTH,
        validators = [validate_name]
        )

    pincode = models.IntegerField(
        'Pincode',
        validators = [validate_pincode]
    )

    state = models.ForeignKey(
        State,
        on_delete = models.CASCADE
    )

    country = models.ForeignKey(
        Country,
        on_delete = models.CASCADE,
    )

    education = models.ManyToManyField(
        Education,
        related_name = 'user'
    )

    certification = models.ManyToManyField(
        Certification,
        related_name = 'user'
    )

    work_detail = models.ManyToManyField(
        WorkDetail,
        related_name = 'user'
    )

    employment_history = models.ManyToManyField(
        EmploymentHistory,
        related_name='users'
    )

    awards = models.ManyToManyField(
        Award,
        related_name='users'
    )

    preference = models.ManyToManyField(
        Preference,
        related_name = 'user'
    )
    def __str__(self):
        return self.name