# Generated by Django 5.0 on 2024-03-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0099_gameport'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ports/'),
        ),
    ]
