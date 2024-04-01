import uuid
from django.db import models

class BaseModel(models.Model):
    MAX_LENGTH = 255
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class SubCategory(BaseModel):
    name = models.CharField("subcategory_name", max_length = BaseModel.MAX_LENGTH)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField("category_name", max_length=BaseModel.MAX_LENGTH)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField("product_name", max_length=BaseModel.MAX_LENGTH)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name