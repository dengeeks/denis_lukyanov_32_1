from django import forms
from store.models import Category, Review


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=64)
    parameters = forms.CharField(max_length=512, widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    category_name = forms.ModelChoiceField(queryset=Category.objects.all())
    price = forms.FloatField()


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name_user', 'comment')
