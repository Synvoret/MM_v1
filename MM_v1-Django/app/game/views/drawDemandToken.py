import random
from django.http import HttpResponse
from dataset.models import DemandTokens


def drawDemandToken(request):
    """Function return new randomly demand token for port."""

    all_tokens = DemandTokens.objects.all()
    random_token = random.choice(all_tokens)

    return HttpResponse(random_token.awers.url)


# def board(request):
#     """Endpoint return a board image."""

#     boardImage = Board.objects.get(name="Board Game")
#     return HttpResponse(boardImage.board.url)