# Generated by Django 5.0 on 2024-01-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0042_alter_shipcard_ship'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipcard',
            name='boats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shipcard',
            name='speed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]