# Generated by Django 5.0 on 2024-03-26 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0084_commandboatcard_supportboatcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandboatcard',
            name='awers',
            field=models.ImageField(blank=True, null=True, upload_to='commandBoatsCards/'),
        ),
        migrations.AlterField(
            model_name='supportboatcard',
            name='awers',
            field=models.ImageField(blank=True, null=True, upload_to='supportBoatsCards/'),
        ),
    ]
