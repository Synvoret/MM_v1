# Generated by Django 5.0 on 2024-01-03 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_rename_game_stackeventscards_game_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackEnemyHitLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('hull', models.IntegerField(default=1)),
                ('cargo', models.IntegerField(default=1)),
                ('masts', models.IntegerField(default=1)),
                ('crew', models.IntegerField(default=1)),
                ('cannons', models.IntegerField(default=1)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
