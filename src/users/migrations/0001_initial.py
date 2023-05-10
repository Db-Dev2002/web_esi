# Generated by Django 4.2 on 2023-05-10 16:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.validators
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.CITIES_CITY_MODEL),
        ("cart", "0002_initial"),
        migrations.swappable_dependency(settings.CITIES_COUNTRY_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="TuxTechUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("N", "Prefer not to say"),
                        ],
                        default="O",
                        max_length=1,
                    ),
                ),
                ("username", models.CharField(max_length=128, null=True, unique=True)),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=128,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "tuxtechuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "nif",
                    models.CharField(blank=True, max_length=16, null=True, unique=True),
                ),
                ("receive_news", models.BooleanField(default=False)),
                (
                    "cart",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cart.info",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("users.tuxtechuser",),
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default="ac2df0f0cb5f4f65ac6b6eb0ff82590f",
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "house_number",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d+[a-zA-Z\\s\\-]*$",
                                message="House number can only contain digits, letters, spaces, and hyphens.",
                            )
                        ],
                    ),
                ),
                (
                    "apartment_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{5}(-\\d{4})?$",
                                message="Postal code must be in the format '12345' or '12345-6789'.",
                            )
                        ],
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.CITIES_CITY_MODEL,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.CITIES_COUNTRY_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CreditCard",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("cardholder_name", models.CharField(max_length=255)),
                (
                    "card_number",
                    models.CharField(
                        max_length=16,
                        validators=[users.validators.validate_card_number],
                    ),
                ),
                (
                    "card_type",
                    models.CharField(
                        choices=[
                            ("VISA", "Visa"),
                            ("MASTERCARD", "Mastercard"),
                            ("UNKNOWN", "Unknown"),
                        ],
                        default="UNKNOWN",
                        max_length=10,
                    ),
                ),
                (
                    "expiry_month",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(12),
                        ]
                    ),
                ),
                (
                    "expiry_year",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(2023)]
                    ),
                ),
                ("cvv", models.CharField(max_length=4)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credit_cards",
                        to="users.client",
                    ),
                ),
            ],
        ),
    ]
