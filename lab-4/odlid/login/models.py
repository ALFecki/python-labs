from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


class Client(AbstractUser):
    email = models.EmailField('email address', unique=True)
    unique_code = models.IntegerField('unique_code', unique=True)
    phone = PhoneNumberField(null=False, region='BY', unique=True)
    city = models.CharField('city', unique=False, max_length=50)
    address = models.CharField('address', unique=False, max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'unique_code', 'phone', 'city', 'address']


