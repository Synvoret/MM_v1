# Generated by Django 5.0 on 2024-01-06 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0044_rename_card_captaincard_captain_and_more'),
        ('game', '0027_playersshipscards'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersCaptainsCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('player_blue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_blue_captain_card', to='dataset.captaincard')),
                ('player_green', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_green_captain_card', to='dataset.captaincard')),
                ('player_red', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_red_captain_card', to='dataset.captaincard')),
                ('player_yellow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_yellow_captain_card', to='dataset.captaincard')),
            ],
        ),
    ]
