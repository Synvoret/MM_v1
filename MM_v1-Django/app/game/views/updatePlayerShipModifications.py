from django.http import JsonResponse
from dataset.models import ShipModifications
from game.models import Game
from game.models import TrackPlayersShipModifications


def updatePlayerShipModifications(request):
    """Endpoint update Player Ship Modifications Token on player board."""

    data = {}

    player_colour = request.GET.get('colour')
    game = Game.objects.get(number=100)
    ship_modifications_track = TrackPlayersShipModifications.objects.get(game_number=game)

    for ship_modification in getattr(ship_modifications_track, f"player_{player_colour}"):
        ship_modification_image = ShipModifications.objects.get(name=ship_modification)
        data[f"{ship_modification.replace(' ', '-').lower()}-image"] = ship_modification_image.awers.url

    return JsonResponse(data)
