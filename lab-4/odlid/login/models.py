from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


class Client(AbstractUser):
    email = models.EmailField("email address", unique=False)
    unique_code = models.PositiveIntegerField("unique_code", unique=False)
    phone = PhoneNumberField(null=False, region="BY", unique=False)
    city = models.CharField("city", unique=False, max_length=50)
    address = models.CharField("address", unique=False, max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "unique_code", "phone", "city", "address"]


