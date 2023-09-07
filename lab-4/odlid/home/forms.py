from django import forms
from .models import Product, ProductModel, ProductCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "code", "model", "image", "cost", "in_prod", "category"]


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name", "image"]


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["name", "year_of_manufacture"]
