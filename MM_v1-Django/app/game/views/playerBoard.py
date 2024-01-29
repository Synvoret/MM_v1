from random import choice
from django.http import JsonResponse
from game.models import Game
from player_board.models import PlayerBoard


def playerBoard(request):
    """Endpoint return a player board image."""

    player_board_image = PlayerBoard.objects.get(name="Player Board")
    player_colour = Game.randomly_player()
    game = Game.objects.get(number=100)
    print(game.player_active_colour, "W PLAYER BOARD")

    data = {
        'playerBoardImage': player_board_image.player_board_image.url,
        'playerColour': player_colour,
    }

    return JsonResponse(data)
