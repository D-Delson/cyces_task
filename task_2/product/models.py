import uuid
from django.db import models

class SubCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField("subcategory_name", max_length=255)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, editable=False)
    name = models.CharField("category_name", max_length=255)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField("product_name", max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name