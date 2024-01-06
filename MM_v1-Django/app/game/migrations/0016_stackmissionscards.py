# Generated by Django 5.0 on 2024-01-04 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0033_alter_sign_image'),
        ('game', '0015_alter_trackenemyhitlocations_hull'),
    ]

    operations = [
        migrations.CreateModel(
            name='StackMissionsCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('mission_1_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataset.missioncard')),
            ],
        ),
    ]