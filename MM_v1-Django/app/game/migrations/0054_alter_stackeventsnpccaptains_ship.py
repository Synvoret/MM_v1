# Generated by Django 5.0 on 2024-01-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0053_stackeventsnpccaptains_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stackeventsnpccaptains',
            name='ship',
            field=models.CharField(blank=True, choices=[('Brig', 'Brig'), ('Flute', 'Flute'), ('Frigate', 'Frigate'), ('Galleon', 'Galleon'), ('Man-o-War', 'Man-o-War'), ('Sloop', 'Sloop')], max_length=50, null=True),
        ),
    ]
