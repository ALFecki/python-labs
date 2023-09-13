from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "discount"]
