# Generated by Django 4.2.1 on 2023-05-15 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("order", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordereditem",
            name="product_variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="product.variant"
            ),
        ),
    ]
