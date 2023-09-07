from django.contrib import admin
from . import models


class ProductModelInline(admin.TabularInline):
    model = models.ProductModel
    raw_id_fields = ["model"]


class ProductCategoryInline(admin.TabularInline):
    model = models.ProductCategory
    raw_id_fields = ["category"]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "cost", "in_prod"]


@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year_of_manufacture"]


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
