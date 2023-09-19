from django.shortcuts import render
# Create your views here.
from store.models import Product,Category


def main_view(request):
    return render(request, template_name='layouts/index.html')


def products_view(request):
    product = Product.objects.all()
    context_data = {
        'products': product
    }
    return render(request, 'products/products.html', context=context_data)


def category_view(request):
    category = Category.objects.all()
    context_data = {
        'categories': category
    }
    return render(request, 'products/categories.html', context=context_data)
