# Generated by Django 5.0 on 2024-01-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0052_alter_eventcard_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcard',
            name='card',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
