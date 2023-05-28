import django_tables2 as tables
from .models import ProductCategory

class ProductTable(tables.Table):
    class Meta:
        model = ProductCategory
        template_name = "django_tables2/bootstrap.html"
        fields = ("image", "name")