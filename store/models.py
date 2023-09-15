from django.db import models
from django.core import validators
from sorl import thumbnail

# Create your models here.

class Store(models.Model):
    image = thumbnail.ImageField(upload_to='store_image',blank=True,null=True)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True)
    parameters = models.TextField(null=True)

    price = models.FloatField()
    rate = models.FloatField(default=5,validators=[validators.MaxValueValidator(5)])
