# Generated by Django 5.1 on 2024-09-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_has_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
