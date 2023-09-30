from django.shortcuts import render, redirect
# Create your views here.
from store.models import Product, Category, Review
from store.forms import ProductCreateForm, ReviewCreateForm


def main_view(request):
    print(request.user.id)
    context_data = {
        'user': request.user
    }
    return render(request, template_name='layouts/index.html',context=context_data)


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
    reviews = Review.objects.filter(product_posted=product.id)
    if request.method == 'GET':
        context_data = {
            'product': product,
            'category': category,
            'reviews': reviews,
            'form': ReviewCreateForm
        }
        return render(request, 'products/details.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = ReviewCreateForm(data)

        if form.is_valid():
            review = form.save(commit=False)
            review.product_posted = product
            form.save()
            return redirect('/products/')
        context_data = {
            'product': product,
            'category': category,
            'reviews': reviews,
            'form': form
        }
        return render(request, 'products/details.html', context=context_data)


def create_products(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)
    if request.method == 'POST':
        data,file = request.POST, request.FILES
        form = ProductCreateForm(data,file)

        if form.is_valid():
            product = form.save(commit=False)
            product.author_name = request.user
            product.save()
            return redirect('/products/')

        context_data = {
            'form': form
        }
        return render(request, 'products/create.html', context=context_data)
