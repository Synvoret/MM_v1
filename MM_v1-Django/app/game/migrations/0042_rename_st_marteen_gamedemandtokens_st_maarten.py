# Generated by Django 5.0 on 2024-01-09 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0041_remove_game_demands_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamedemandtokens',
            old_name='st_marteen',
            new_name='st_maarten',
        ),
    ]