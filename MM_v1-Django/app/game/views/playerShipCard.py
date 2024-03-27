from django.http import JsonResponse
from game.models import Game
from dataset.models import ShipCard
from game.models import PlayersShipsCards


def playerShipCard(request):
    """Endpoint gives a player ship card."""

    data = []

    colour = request.GET.get('colour')
    game = Game.objects.get(number=100)
    player_ship = PlayersShipsCards.objects.get(game_number=game)
    player_ship_instance = getattr(player_ship, f"player_{colour}")

    data = {
        "shipCardImage": player_ship_instance.awers.url,
    }

    return JsonResponse(data)
