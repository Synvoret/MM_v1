from django.http import HttpResponse, JsonResponse
from dataset.models import Cube
from game.models import TrackLoyality


def loyalityTrackCube(request):
    """Endpoint back cubes to track crew loyality."""

    colour = request.GET.get('colour', None)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    values = TrackLoyality.objects.get(game_number=1)
    if colour == 'blue':
        loyality_value = (values.player_blue).lower()
    if colour == 'green':
        loyality_value = (values.player_green).lower()
    if colour == 'red':
        loyality_value = (values.player_red).lower()
    if colour == 'yellow':
        loyality_value = (values.player_yellow).lower()

    data = {
        "cubeImage": colour_cube_image,
        "loyalityValue": loyality_value,
    }

    return JsonResponse(data)
