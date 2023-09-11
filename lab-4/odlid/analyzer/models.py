from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from login.models import Client

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField("date", null=False)
    star_count = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(null=False)
