# Generated by Django 5.0 on 2024-02-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0082_alter_shipslocalisations_blue_ship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stackeventsnpccaptains',
            name='game_round',
            field=models.IntegerField(default=0),
        ),
    ]
