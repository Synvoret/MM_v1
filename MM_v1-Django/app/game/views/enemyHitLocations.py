from django.http import HttpResponse
from dataset.models import Cube


def enemyHitLocation(request):
    """Endpoint put all cubes on 1 at track Enemy Hit Locations."""

    cube = Cube.objects.get(name='Brown Cube')

    return HttpResponse(cube.image.url)
