from django.http import HttpResponse, JsonResponse
from dataset.models import Cube
from game.models import Game
from game.models import TrackPlayerHitLocations


def playerHitLocation(request):
    """Endpoint put all cubes on track Player Hit Locations."""

    colour = request.GET.get('colour', None)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    hits = TrackPlayerHitLocations.objects.get(player_colour=colour.capitalize())

    data = {
        "cubeImage": colour_cube_image,
        "hullHit": hits.hull,
        "cargoHit": hits.cargo,
        "mastsHit": hits.masts,
        "crewHit": hits.crew,
        "cannonsHit": hits.cannons,
    }

    return JsonResponse(data)
