from django.db import models
from django.core import validators
from sorl import thumbnail


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = thumbnail.ImageField(upload_to='store_image', blank=True, null=True)
    title = models.CharField(max_length=64)
    parameters = models.TextField(null=True)
    category_name = models.ManyToManyField(Category,related_name='product')

    price = models.FloatField()
    rate = models.FloatField(default=5, validators=[validators.MaxValueValidator(5)])
