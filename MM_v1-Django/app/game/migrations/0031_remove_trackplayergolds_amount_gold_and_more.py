# Generated by Django 5.0 on 2024-01-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0030_remove_playersglorycards_player_blue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackplayergolds',
            name='amount_gold',
        ),
        migrations.RemoveField(
            model_name='trackplayergolds',
            name='player_colour',
        ),
        migrations.AddField(
            model_name='trackplayergolds',
            name='player_blue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trackplayergolds',
            name='player_green',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trackplayergolds',
            name='player_red',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trackplayergolds',
            name='player_yellow',
            field=models.IntegerField(default=0),
        ),
    ]