from django import forms
from store.models import Review, Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'title', 'parameters', 'description', 'category_name', 'price')


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name_user', 'comment')
