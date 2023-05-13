# Generated by Django 4.2.1 on 2023-05-13 15:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import product.models.variant
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseInfo",
            fields=[
                ("name", models.TextField()),
                (
                    "ref",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "name",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("logo_hash", models.CharField(default=" ", max_length=64)),
                ("logo_type", models.CharField(max_length=4)),
                (
                    "logo",
                    models.ImageField(
                        upload_to="logos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["png", "svg"],
                                message="File format not supported.",
                            )
                        ],
                    ),
                ),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "name",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        upload_to="categories/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["png", "svg"],
                                message="File format not supported.",
                            )
                        ],
                    ),
                ),
                ("_sku_prefix", models.CharField(editable=False, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("hash", models.CharField(default=" ", max_length=64)),
                ("media_type", models.CharField(max_length=4)),
                (
                    "image",
                    models.ImageField(
                        null=True,
                        upload_to="products/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "gif"],
                                message="File format not supported.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                (
                    "Id",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("price_to_add", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Specification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=32)),
                ("value", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "name",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("description", models.TextField()),
                ("_sku_prefix", models.CharField(editable=False, max_length=2)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_category",
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Variant",
            fields=[
                ("ean", models.CharField(editable=False, max_length=14, unique=True)),
                (
                    "sku",
                    models.CharField(
                        default=product.models.variant.generate_unique_sku,
                        editable=False,
                        max_length=32,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_default", models.BooleanField(default=False)),
                ("name", models.TextField()),
                ("mediafiles_hash", models.CharField(max_length=64)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("altered_specs", models.JSONField(editable=False, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Variant",
                        to="product.baseinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VariantMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pos", models.PositiveSmallIntegerField()),
                (
                    "media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.media"
                    ),
                ),
                (
                    "variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.variant",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="variant",
            name="media",
            field=models.ManyToManyField(
                through="product.VariantMedia", to="product.media"
            ),
        ),
        migrations.AddField(
            model_name="variant",
            name="specifications",
            field=models.ManyToManyField(to="product.specification"),
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "serial",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="units",
                        to="order.order",
                    ),
                ),
                (
                    "variant_id",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instances",
                        to="product.variant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "name",
                    models.CharField(max_length=64, primary_key=True, serialize=False),
                ),
                ("description", models.TextField()),
                ("_sku_prefix", models.CharField(editable=False, max_length=2)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="type",
                        to="product.subcategory",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="specification",
            constraint=models.UniqueConstraint(
                fields=("key", "value"), name="unique_key_value"
            ),
        ),
        migrations.AddField(
            model_name="option",
            name="spec_id",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.specification",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_baseInfo",
                to="product.brand",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.category",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="ptype",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.type",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="subCategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.subcategory",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="variantmedia",
            unique_together={("variant", "media")},
        ),
    ]
