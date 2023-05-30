from django import forms
from .models import Product, ProductModel


class ProductForm(forms.ModelForm):
    # model = (m.name for m in ProductModel.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'code', 'model', 'cost', 'in_prod', 'category']