"""
URL configuration for OnlineStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views as view
from django.conf import settings
from django.conf.urls.static import static
from auth_user import views as auth_view

...

# Эти строки — в самый конец файла:


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view.main_view, name='main-menu'),

    #products
    path("products/", view.products_view,name='product_menu'),
    path('products/create/', view.create_products,name='create_product'),
    path('products/<slug:slug_product>/', view.get_full_info_of_product,name='full_info'),

    #category
    path('category/',view.category_view,name='category_menu'),
    path('category/<int:category_id>/',view.get_products_by_category,name='category_name'),

    #users_auth
    path('users/registration/',auth_view.register_view,name='register'),
    path('users/login/',auth_view.login_view,name='login'),
    path('users/logout/',auth_view.logout_view,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
