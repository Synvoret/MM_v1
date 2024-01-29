from game.models import Game


def next_player():
    """
    Method return next player for playing his actions in current round,
    in order blue, green, red, yellow.

    Return: Player colour: 'blue', 'green', 'red' or 'yellow'.
    """
    game = Game.objects.get(number=100)
    players = {
        'blue': (game.player_blue_play, game.player_blue_done),
        'green': (game.player_green_play, game.player_green_done),
        'red': (game.player_red_play, game.player_red_done),
        'yellow': (game.player_yellow_play, game.player_yellow_done),
    }

    if players['blue'][0]:
        if not players['blue'][1]:
            game.player_active_colour = 'blue'
            game.save()
            return 'blue'
    elif players['green'][0]:
        if not players['green'][1]:
            game.player_active_colour = 'green'
            game.save()
            return 'green'
    elif players['red'][0]:
        if not players['red'][1]:
            game.player_active_colour = 'red'
            game.save()
            return 'red'
    elif players['yellow'][0]:
        if not players['yellow'][1]:
            game.player_active_colour = 'yellow'
            game.save()
            return 'yellow'
