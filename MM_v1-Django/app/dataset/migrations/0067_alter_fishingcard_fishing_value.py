# Generated by Django 5.0 on 2024-01-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0066_fishingcard_fishing_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishingcard',
            name='fishing_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
