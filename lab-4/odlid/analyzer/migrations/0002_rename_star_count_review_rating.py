# Generated by Django 4.2.1 on 2023-09-12 07:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("analyzer", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="star_count",
            new_name="rating",
        ),
    ]
