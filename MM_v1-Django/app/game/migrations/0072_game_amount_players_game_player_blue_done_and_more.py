# Generated by Django 5.0 on 2024-01-30 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0071_alter_trackenemyhitlocations_cannons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='amount_players',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='player_blue_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_blue_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_green_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_green_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_red_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_red_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_yellow_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player_yellow_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='rounds',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='PlayersActionsFlow',
        ),
    ]
