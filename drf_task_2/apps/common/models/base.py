from django.db import models
from django.core.validators import RegexValidator

class AppManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Base(models.Model):
    create_at = models.DateTimeField(
        'created',
        auto_now_add = True
    )

    updated_at = models.DateTimeField(
        'updated',
        auto_now = True
    )

    is_active = models.BooleanField(
        default = True
    )

    objects = AppManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True

#validators.py

def validate_name(value):
    return RegexValidator(
                regex = '^[A-Za-z\s]*$',
                message = 'Name should only contain letters [a-z, A-Z]'
                )

def validate_pincode(value):
    return RegexValidator(
                regex = '^\d{6}$',
                message = 'Enter the valid Pincode!'
    )

def validate_year(value):
    return 
