# Generated by Django 4.2.1 on 2023-05-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_product_category_alter_product_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productcategory",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="resources/images"
            ),
        ),
    ]
