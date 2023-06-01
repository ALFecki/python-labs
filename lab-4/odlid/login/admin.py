from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'city', 'address']




