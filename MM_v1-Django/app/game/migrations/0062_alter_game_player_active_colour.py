# Generated by Django 5.0 on 2024-01-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0061_alter_game_player_active_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_active_colour',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
