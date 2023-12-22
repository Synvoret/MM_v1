from random import randint
from django.db import models


class Game(models.Model):
    """Game identifacator."""

    def random_number_game():
        """Generate randomly number for new game."""

        used_numbers = set(Game.objects.values_list('number', flat=True))

        while True:
            random_number = randint(100, 999)
            if random_number not in used_numbers:
                return random_number

    number = models.IntegerField(default=random_number_game, unique=True)
    amount_players = models.IntegerField(default=1)
    rounds = models.IntegerField(default=0)

    def __str__(self):
        return f"Game number - {self.number}"
