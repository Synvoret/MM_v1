# Generated by Django 5.0 on 2024-01-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_alter_trackenemyhitlocations_game_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='hull',
            field=models.IntegerField(default=4),
        ),
    ]