# Generated by Django 5.0 on 2024-01-03 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_alter_game_round'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stackeventscards',
            old_name='game',
            new_name='game_number',
        ),
    ]
