# Generated by Django 5.0 on 2023-12-31 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(
                max_length=100,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
        ),
    ]
