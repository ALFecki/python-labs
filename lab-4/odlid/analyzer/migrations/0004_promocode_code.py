# Generated by Django 4.2.1 on 2023-11-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analyzer", "0003_promocode"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocode",
            name="code",
            field=models.IntegerField(default=1002),
            preserve_default=False,
        ),
    ]
