# Generated by Django 5.0 on 2024-01-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0024_dice'),
    ]

    operations = [
        migrations.AddField(
            model_name='dice',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]