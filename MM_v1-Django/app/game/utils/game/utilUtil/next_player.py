from game.models import Game


def next_player() -> str:
    """
    Method return next player for playing his actions in current round,
    in order blue, green, red, yellow.

    Return: 'blue', 'green', 'red' or 'yellow'.
    """
    game = Game.objects.get(number=100)

    players = {
        'blue': (game.player_blue_play, game.player_blue_done),
        'green': (game.player_green_play, game.player_green_done),
        'red': (game.player_red_play, game.player_red_done),
        'yellow': (game.player_yellow_play, game.player_yellow_done),
    }

    # if player exist and didn't play actions in round
    if game.player_blue_play and not game.player_blue_done:
        return 'blue'
    elif game.player_green_play and not game.player_green_done:
        return 'green'
    elif game.player_red_play and not game.player_red_done:
        return 'red'
    elif game.player_yellow_play and not game.player_yellow_done:
        return 'yellow'
    else:
        for player in players.keys():
            if players[player][0]:
                setattr(game, f'player_{player}_done', False)
        game.save()

        return next_player()
