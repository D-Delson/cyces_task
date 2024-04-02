import uuid
from django.db import models
from django.core.validators import DecimalValidator, MinLengthValidator

from .config import MAX_LENGTH, MODEL_EMPTY_FIELD_ERROR_MSG


class BaseModelManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset().filter(deleted=False)
        return queryset.order_by('-updated').annotate(s_no=models.Count('pk') + 1)

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default = False)
    objects = BaseModelManager()

    def delete(self):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True


class SubCategory(BaseModel):
    name = models.CharField("subcategory_name", 
                            max_length = MAX_LENGTH,
                            blank = False,
                            validators = [MinLengthValidator(3, message= MODEL_EMPTY_FIELD_ERROR_MSG)]
                            )
    
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField("category_name", 
                            max_length = MAX_LENGTH,
                            validators = [MinLengthValidator(3, message= MODEL_EMPTY_FIELD_ERROR_MSG)]
                            )
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Product(BaseModel):
    name = models.CharField("product_name",
                            max_length = MAX_LENGTH,
                            validators = [MinLengthValidator(3, message= MODEL_EMPTY_FIELD_ERROR_MSG)])
    price = models.DecimalField(max_digits = 5, decimal_places = 2, validators = [DecimalValidator(5, 2)])
    category = models.ForeignKey('Category', on_delete  = models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete = models.CASCADE)

    def __str__(self):
        return self.name