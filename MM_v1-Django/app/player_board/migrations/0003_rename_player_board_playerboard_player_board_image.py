# Generated by Django 5.0 on 2024-01-05 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_board', '0002_playerboard_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerboard',
            old_name='player_board',
            new_name='player_board_image',
        ),
    ]