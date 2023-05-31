from django import forms
from .models import Product, ProductModel


class ProductForm(forms.ModelForm):
    # model = (m.name for m in ProductModel.objects.all())
    all_model = ProductModel.objects.values()
    choices = [(m['name'] for m in all_model)]
    model = forms.ChoiceField(choices=choices, required=False )
    class Meta:
        model = Product
        fields = ['name', 'code', 'model', 'cost', 'in_prod', 'category']