from random import choice
from game.models import Game


def randomly_player() -> str:
    """
    Method choose randomly player for playing his actions in current round.

    players_in_play: dict with colours players in play.
    return: 'blue', 'green', 'red' or 'yellow'.
    """

    game = Game.objects.get(number=100)

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
                return random_player_colour
