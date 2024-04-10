from django.db import models
from django.core.validators import RegexValidator

class AppManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    objects = AppManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True


def name_validator(value):
    return RegexValidator(regex='^[A-Za-z\s]*$', message='only a-z')(value)

         




