# Generated by Django 5.0 on 2024-01-09 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0046_eventcard_leadership_eventcard_npc_name_and_more'),
        ('game', '0044_gamedemandtokens_gulf_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StackLargePirate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('large_pirate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataset.eventcard')),
            ],
        ),
    ]
