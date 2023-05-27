from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import ProductTable

class ProductListView(SingleTableView):
    model = Product
    table_class = ProductTable
    template_name = 'list.html'
