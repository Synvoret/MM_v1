# Generated by Django 5.0 on 2024-02-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0078_alter_shipslocalisations_merchants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipslocalisations',
            name='merchants',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]