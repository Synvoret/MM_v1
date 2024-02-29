# Generated by Django 5.0 on 2024-02-23 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0087_trackmerchanttokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackPlayerShipModifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_blue', models.JSONField(blank=True, default=list, null=True)),
                ('player_green', models.JSONField(blank=True, default=list, null=True)),
                ('player_red', models.JSONField(blank=True, default=list, null=True)),
                ('player_yellow', models.JSONField(blank=True, default=list, null=True)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
