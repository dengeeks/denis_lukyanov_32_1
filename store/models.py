from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    icon = models.ImageField(upload_to='category_icon', blank=True, null=True)
    title = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    product_posted = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    name_user = models.CharField(max_length=32)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Product(models.Model):
    author_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='store_image', blank=True, null=True)
    title = models.CharField(max_length=64)
    parameters = models.TextField()
    description = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)

    price = models.FloatField()

    def __str__(self):
        return self.title
