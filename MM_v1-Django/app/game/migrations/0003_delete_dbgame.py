# Generated by Django 5.0 on 2023-12-25 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_remove_game_rounds_dbgame'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DBGame',
        ),
    ]
