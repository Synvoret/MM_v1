from django.http import HttpResponse
from player_board.models import PlayerBoard


def player_board(request):
    """Endpoint return a player board image."""

    boardImage = PlayerBoard.objects.get(name="Player Board")
    return HttpResponse(boardImage.player_board_image.url)
