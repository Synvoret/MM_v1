# Generated by Django 5.0 on 2024-02-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0080_rename_merchants_shipslocalisations_merchants_ship'),
    ]

    operations = [
        migrations.AddField(
            model_name='stackmissionscards',
            name='game_round',
            field=models.IntegerField(default=0),
        ),
    ]
