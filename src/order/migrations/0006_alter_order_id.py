# Generated by Django 4.2.1 on 2023-05-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default='b8aaee0fbef9411fb7ab77a8dfa202bf', editable=False, primary_key=True, serialize=False),
        ),
    ]
