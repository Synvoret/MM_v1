from django.http import JsonResponse
from dataset.models import Cube
from game.models import TrackPlayerHitLocations


def playerHitLocation(request):
    """Endpoint put all cubes on track Player Hit Locations."""

    data = {}

    colour = request.GET.get('colour', None)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    hits = TrackPlayerHitLocations.objects.get(player_colour=colour.capitalize())

    data["cubeImage"] = colour_cube_image
    data["hullHit"] = hits.hull
    data["cargoHit"] = hits.cargo
    data["mastsHit"] = hits.masts
    data["crewHit"] = hits.crew
    data["cannonsHit"] = hits.cannons

    return JsonResponse(data)
