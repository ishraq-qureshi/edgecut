from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=90)
    price = models.FloatField()
    image = models.ImageField(upload_to='uploads/products')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name