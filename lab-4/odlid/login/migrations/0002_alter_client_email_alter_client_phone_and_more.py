# Generated by Django 4.2.1 on 2023-06-01 07:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email address"),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region="BY"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="unique_code",
            field=models.IntegerField(verbose_name="unique_code"),
        ),
    ]
