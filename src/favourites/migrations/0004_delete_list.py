# Generated by Django 4.1.7 on 2023-03-30 19:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("favourites", "0003_info_remove_list_user_alter_item_cart"),
        ("users", "0004_alter_client_favourites"),
    ]

    operations = [
        migrations.DeleteModel(
            name="List",
        ),
    ]
