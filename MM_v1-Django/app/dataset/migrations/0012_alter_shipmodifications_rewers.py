# Generated by Django 5.0 on 2023-12-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0011_alter_shipmodifications_rewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmodifications',
            name='rewers',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='shipModifications/'),
        ),
    ]
