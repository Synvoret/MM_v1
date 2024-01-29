from random import randint, choice
from django.db import models, transaction
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS


class Game(models.Model):
    """Game identifacator."""

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

    player_active_colour = models.CharField(max_length=30, null=True, blank=True, choices=PLAYER_COLOURS)


    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Game". Before new game."""
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
            field.player_active_colour = None
            field.save()

    @classmethod
    def randomly_player(cls):
        """
        Method choose randomly player for playing his actions in current round.

        return: Player colour: 'blue', 'green', 'red' or 'yellow'.
        """
        game = cls.objects.get(number=100)
        players = {
            'blue': (game.player_blue_play, game.player_blue_done),
            'green': (game.player_green_play, game.player_green_done),
            'red': (game.player_red_play, game.player_red_done),
            'yellow': (game.player_yellow_play, game.player_yellow_done),
        }

        while True:
            random_player_colour = choice(list(players.keys()))
            if players[random_player_colour][0]: # True if player in game
                if not players[random_player_colour][1]: # False if player didn't play his
                    game.player_active_colour = random_player_colour
                    game.save()
                    return random_player_colour

    def __str__(self):
        return f"Game number - {self.number}"
