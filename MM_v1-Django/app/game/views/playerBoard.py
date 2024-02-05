from django.http import JsonResponse
from player_board.models import PlayerBoard


def playerBoard(request):
    """Endpoint return a player board image."""

    player_board_image = PlayerBoard.objects.get(name="Player Board")

    print(dict(request.session), 'PLAYER BOARD')

    data = {
        'playerBoardImage': player_board_image.player_board_image.url,
        'playerColour': request.session['playerColourActive'],
    }

    return JsonResponse(data)
