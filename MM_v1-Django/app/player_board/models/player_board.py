from django.db import models
from game.models import Game


class PlayerBoard(models.Model):
    """Player Board database."""

    class Meta:
        verbose_name = 'Player Board'

    COLOUR = [
        ("Blue", "Blue"),
        ("Green", "Green"),
        ("Red", "Red"),
        ("Yellow", "Yellow"),
    ]

    # colour = models.CharField(max_length=10, null=True, blank=True, choices=COLOUR)
    name = models.CharField(max_length=150, default='Player Board')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    player_board_image = models.ImageField(upload_to='player_board/', null=True, blank=True)

    def __str__(self):
        return f"Player Board for game nr. {self.game.number}"
