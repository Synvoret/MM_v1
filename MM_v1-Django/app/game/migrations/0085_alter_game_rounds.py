# Generated by Django 5.0 on 2024-02-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0084_alter_game_rounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rounds',
            field=models.IntegerField(unique=True),
        ),
    ]