# Generated by Django 5.0 on 2024-01-08 13:24

import game.models.game
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0036_alter_game_demands_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='demands_token',
            field=models.JSONField(blank=True, default=game.models.game.Game.sea_zones_list, null=True),
        ),
    ]
