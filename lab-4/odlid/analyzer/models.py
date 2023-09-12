from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from login.models import Client
from datetime import datetime, timezone


class Review(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField("date", null=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(null=False)
