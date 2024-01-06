from django.http import HttpResponse, JsonResponse
from dataset.models import Cube
from game.models import Game
from game.models import TrackEnemyHitLocations


def enemyHitLocation(request):
    """Endpoint put all cubes on 1 at track Enemy Hit Locations."""

    cube = Cube.objects.get(name='Brown Cube')
    cube_image = cube.image.url

    hits = TrackEnemyHitLocations.objects.get(game_number=1)

    data = {
        "cubeImage": cube_image,
        "hullHit": hits.hull,
        "cargoHit": hits.cargo,
        "mastsHit": hits.masts,
        "crewHit": hits.crew,
        "cannonsHit": hits.cannons,
    }

    return JsonResponse(data)
