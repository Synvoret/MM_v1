from django.http import HttpResponse
from board.models import Board


def board(request):
    """Endpoint return a board image."""

    boardImage = Board.objects.get(name="Board Game")
    return HttpResponse(boardImage.board.url)
