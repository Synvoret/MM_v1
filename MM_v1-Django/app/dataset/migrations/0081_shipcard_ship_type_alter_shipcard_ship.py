# Generated by Django 5.0 on 2024-03-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0080_alter_tile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipcard',
            name='ship_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipcard',
            name='ship',
            field=models.CharField(blank=True, choices=[('Brig', 'Brig'), ('Flute', 'Flute'), ('Frigate', 'Frigate'), ('Galleon', 'Galleon'), ('Man-o-War', 'Man-o-War'), ('Sloop', 'Sloop')], max_length=50, null=True),
        ),
    ]
