# Generated by Django 5.0 on 2024-01-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0032_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='signs/'),
        ),
    ]
