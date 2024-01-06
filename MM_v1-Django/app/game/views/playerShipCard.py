from django.http import HttpResponse, JsonResponse
from game.models import Game
from dataset.models import ShipCard
from game.models import PlayersShipsCards


def playerShipCard(request):
    """Endpoint gives a player ship card."""

    colour = request.GET.get('colour', None)
    player_ship = PlayersShipsCards.objects.get(pk=1)

    if colour == 'blue':
        player_ship = player_ship.player_blue
    if colour == 'green':
        player_ship = player_ship.player_green
    if colour == 'red':
        player_ship = player_ship.player_red
    if colour == 'yellow':
        player_ship = player_ship.player_yellow

    ship = ShipCard.objects.get(ship=player_ship.ship)

    data = {
        "shipCardImage": ship.awers.url,
    }

    return JsonResponse(data)
