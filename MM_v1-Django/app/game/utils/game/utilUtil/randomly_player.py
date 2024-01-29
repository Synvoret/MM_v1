from random import choice


def randomly_player(players_in_play: dict) -> str:
    """
    Method choose randomly player for playing his actions in current round.

    players_in_play: dict with colours players in play.
    return: Player colour: 'blue', 'green', 'red' or 'yellow'.
    """

    while True:
        random_player_colour = choice(list(players_in_play.keys()))
        if players_in_play[random_player_colour][0]: # True if player in game
            if not players_in_play[random_player_colour][1]: # False if player didn't play his
                return random_player_colour
