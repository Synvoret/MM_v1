from django.http import HttpResponse
from dataset.models import Cube


def gloryTrackCube(request):
    """Endpoint put all cubes on 0 at track Glory Points."""

    colour = request.GET.get('colour', None)

    name = colour.capitalize() + ' Cube'
    cube = Cube.objects.get(name=name)

    return HttpResponse(cube.image.url)
