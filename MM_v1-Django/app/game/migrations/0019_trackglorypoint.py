# Generated by Django 5.0 on 2024-01-04 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_alter_stackmissionscards_game_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackGloryPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('player_1', models.IntegerField(default=1)),
                ('player_2', models.IntegerField(default=2)),
                ('player_3', models.IntegerField(default=3)),
                ('player_4', models.IntegerField(default=4)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
