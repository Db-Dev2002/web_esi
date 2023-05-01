# Generated by Django 4.2 on 2023-04-30 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                upload_to="media/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png", "svg"],
                        message="File format not supported.",
                    )
                ],
            ),
        ),
    ]
