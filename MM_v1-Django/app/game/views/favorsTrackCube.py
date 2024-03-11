from django.http import JsonResponse
from dataset.models import Cube
from game.models import TrackFavors


def favorsTrackCube(request):
    """Endpoint back cubes to track favors."""

    colour = request.GET.get('colour', None)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    values = TrackFavors.objects.get(game_number=1)
    if colour == 'blue':
        favor_value = str(values.player_blue).lower()
    if colour == 'green':
        favor_value = str(values.player_green).lower()
    if colour == 'red':
        favor_value = str(values.player_red).lower()
    if colour == 'yellow':
        favor_value = str(values.player_yellow).lower()

    data = {
        "cubeImage": colour_cube_image,
        "favourValue": favor_value,
    }

    return JsonResponse(data)
