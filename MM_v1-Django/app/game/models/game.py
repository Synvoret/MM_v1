from random import randint
from django.db import models


class Game(models.Model):
    """Game identifacator."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Game"."""
        fields = cls.objects.all()
        for field in fields:
            field.amount_players = 0
            field.round = 0
            field.player_blue_play = False
            field.player_blue_done = False
            field.player_green_play = False
            field.player_green_done = False
            field.player_red_play = False
            field.player_red_done = False
            field.player_yellow_play = False
            field.player_yellow_done = False
            field.save()

    @classmethod
    def check_players_in_game(cls):
        """Method checking players in game and current playing round."""
        game = cls.objects.get(number=100)
        current_round = game.round

    def sea_zones_list():
        sea_zones_list = {}
        return sea_zones_list

    def random_number_game():
        """Generate randomly number for new game."""

        used_numbers = set(Game.objects.values_list('number', flat=True))

        while True:
            random_number = randint(100, 999)
            if random_number not in used_numbers:
                return random_number

    number = models.IntegerField(default=random_number_game, unique=True)
    amount_players = models.IntegerField(default=0)
    round = models.IntegerField(default=0)

    player_blue_play = models.BooleanField(default=False)
    player_blue_done = models.BooleanField(default=False)

    player_green_play = models.BooleanField(default=False)
    player_green_done = models.BooleanField(default=False)

    player_red_play = models.BooleanField(default=False)
    player_red_done = models.BooleanField(default=False)

    player_yellow_play = models.BooleanField(default=False)
    player_yellow_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Game number - {self.number}"
