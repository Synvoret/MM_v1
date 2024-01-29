# Generated by Django 5.0 on 2024-01-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0060_alter_game_player_active_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_active_colour',
            field=models.CharField(blank=True, choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red'), ('yellow', 'yellow')], max_length=30, null=True),
        ),
    ]
