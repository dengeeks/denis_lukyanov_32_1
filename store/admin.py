from django.contrib import admin
from store.models import Product, Category,Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'parameters', 'category_name')


admin.site.register(Category)
admin.site.register(Review)