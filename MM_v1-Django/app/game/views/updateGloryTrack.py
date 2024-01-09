from django.http import JsonResponse
from dataset.models import Cube
from game.models import TrackGloryPoint


def updateGloryTrack(request):
    """Endpoint back cubes to track Glory Points."""

    colour = request.GET.get('colour', None)

    values = TrackGloryPoint.objects.get(game_number=1)

    if colour == 'blue':
        blue_cube = Cube.objects.get(name='Blue Cube')
        cube_image = blue_cube.image.url
        amount_glory_point = values.player_blue
    if colour == 'green':
        green_cube = Cube.objects.get(name='Green Cube')
        cube_image = green_cube.image.url
        amount_glory_point = values.player_green
    if colour == 'red':
        red_cube = Cube.objects.get(name='Red Cube')
        cube_image = red_cube.image.url
        amount_glory_point = values.player_red
    if colour == 'yellow':
        yellow_cube = Cube.objects.get(name='Yellow Cube')
        cube_image = yellow_cube.image.url
        amount_glory_point = values.player_yellow

    data = {
        "cubeImage": cube_image,
        "amountGloryPoint": str(amount_glory_point),
    }

    return JsonResponse(data)
