# Generated by Django 5.0 on 2024-01-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0025_dice_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dice',
            name='value',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
