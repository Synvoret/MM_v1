from django.db import models
from .game import Game


class TrackLoyality(models.Model):
    """Presents a track for crew loyality."""

    LOYALITY = [
        ('Fierce Loyality', 'Fierce Loyality'),
        ('Happy', 'Happy'),
        ('Pleased', 'Pleased'),
        ('Content', 'Content'),
        ('Restless', 'Restless'),
        ('Unhappy', 'Unhappy'),
        ('Angry', 'Angry'),
        ('Mutiny', 'Mutiny'),
    ]

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    player_blue = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_green = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_red = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_yellow = models.CharField(max_length=20, default='Content', choices=LOYALITY)

    def __str__(self):
        return f"Track Crew Loyality."
