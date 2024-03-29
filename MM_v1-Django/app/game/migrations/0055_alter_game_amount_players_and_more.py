# Generated by Django 5.0 on 2024-01-19 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0061_eventcard_moving'),
        ('game', '0054_alter_stackeventsnpccaptains_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='amount_players',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerscaptainscards',
            name='player_blue',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_blue_captain_card', to='dataset.captaincard'),
        ),
        migrations.AlterField(
            model_name='playerscaptainscards',
            name='player_green',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_green_captain_card', to='dataset.captaincard'),
        ),
        migrations.AlterField(
            model_name='playerscaptainscards',
            name='player_red',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_red_captain_card', to='dataset.captaincard'),
        ),
        migrations.AlterField(
            model_name='playerscaptainscards',
            name='player_yellow',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_yellow_captain_card', to='dataset.captaincard'),
        ),
    ]
