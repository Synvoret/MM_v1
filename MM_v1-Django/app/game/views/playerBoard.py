from django.http import JsonResponse
from game.models import Game
from player_board.models import PlayerBoard


def playerBoard(request):
    """Endpoint return a player board image."""

    game = Game.objects.get(number=100)
    player_board_image = PlayerBoard.objects.get(name="Player Board")
    # print(player_captains.player_yellow)
    game.check_players_in_game()

    player_colour = 'yellow'

    data = {
        'playerBoardImage': player_board_image.player_board_image.url,
        'playerColour': player_colour,
    }

    return JsonResponse(data)
