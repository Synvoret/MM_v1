# Generated by Django 5.0 on 2023-12-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0007_shipmodifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmodifications',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
