from django.http import JsonResponse
from game.models import Game
from dataset.models import CaptainCard
from game.models import PlayersCaptainsCards


def playerCaptainCard(request):
    """Endpoint gives a player ship card."""

    colour = request.GET.get('colour', None)
    player_captain = PlayersCaptainsCards.objects.get(pk=1)

    if colour == 'blue':
        player_captain = player_captain.player_blue
    if colour == 'green':
        player_captain = player_captain.player_green
    if colour == 'red':
        player_captain = player_captain.player_red
    if colour == 'yellow':
        player_captain = player_captain.player_yellow

    captain = CaptainCard.objects.get(captain=player_captain.captain)

    data = {
        "captainCardImage": captain.awers.url,
    }

    return JsonResponse(data)
