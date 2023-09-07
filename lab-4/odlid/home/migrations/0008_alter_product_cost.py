# Generated by Django 4.2.1 on 2023-05-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_alter_product_cost_alter_product_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="cost",
            field=models.DecimalField(
                decimal_places=2, help_text="Enter product cost", max_digits=10
            ),
        ),
    ]
