from django.shortcuts import render
# Create your views here.
from store.models import Product, Category


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


def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_name_id=category_id)
    context_data = {
        'products': products
    }
    return render(request, 'products/prods_by_category.html', context=context_data)


def get_full_info_of_product(request, slug_product):
    product = Product.objects.get(slug=slug_product)
    category = Category.objects.get(id=product.category_name_id)
    context_data = {
        'product': product,
        'category': category
    }
    return render(request, 'products/details.html', context=context_data)
