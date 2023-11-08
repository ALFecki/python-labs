from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from login.models import Client


class Review(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField("date", null=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(null=False)


class PromoCode(models.Model):
    name = models.TextField(null=False)
    code = models.IntegerField()
    is_active = models.BooleanField(null=False, default=True)
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])