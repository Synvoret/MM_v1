# Generated by Django 5.0 on 2024-01-06 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0022_alter_game_amount_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackLoyality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('player_blue', models.CharField(choices=[('Fierce Loyality', 'Fierce Loyality'), ('Happy', 'Happy'), ('Pleased', 'Pleased'), ('Content', 'Content'), ('Restless', 'Restless'), ('Unhappy', 'Unhappy'), ('Angry', 'Angry'), ('Mutiny', 'Mutiny')], default='Content', max_length=20)),
                ('player_green', models.CharField(choices=[('Fierce Loyality', 'Fierce Loyality'), ('Happy', 'Happy'), ('Pleased', 'Pleased'), ('Content', 'Content'), ('Restless', 'Restless'), ('Unhappy', 'Unhappy'), ('Angry', 'Angry'), ('Mutiny', 'Mutiny')], default='Content', max_length=20)),
                ('player_red', models.CharField(choices=[('Fierce Loyality', 'Fierce Loyality'), ('Happy', 'Happy'), ('Pleased', 'Pleased'), ('Content', 'Content'), ('Restless', 'Restless'), ('Unhappy', 'Unhappy'), ('Angry', 'Angry'), ('Mutiny', 'Mutiny')], default='Content', max_length=20)),
                ('player_yellow', models.CharField(choices=[('Fierce Loyality', 'Fierce Loyality'), ('Happy', 'Happy'), ('Pleased', 'Pleased'), ('Content', 'Content'), ('Restless', 'Restless'), ('Unhappy', 'Unhappy'), ('Angry', 'Angry'), ('Mutiny', 'Mutiny')], default='Content', max_length=20)),
                ('game_number', models.ForeignKey(blank=True, default=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
