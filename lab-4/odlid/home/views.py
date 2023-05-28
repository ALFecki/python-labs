from django.shortcuts import render
from .models import ProductCategory
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import ProductTable


class ProductCategoryView(SingleTableView):
    model = ProductCategory
    table_class = ProductTable
    template_name = "list.html"
