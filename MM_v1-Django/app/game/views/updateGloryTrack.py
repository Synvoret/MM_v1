from django.http import JsonResponse
from dataset.models import Cube
from game.models import TrackGloryPoint


def updateGloryTrack(request):
    """Endpoint back cubes to track Glory Points."""

    values = TrackGloryPoint.objects.get(game_number=1)

    blue_cube = Cube.objects.get(name='Blue Cube')
    blue_cube_image = blue_cube.image.url
    player_blue_amount = values.player_blue
    green_cube = Cube.objects.get(name='Green Cube')
    green_cube_image = green_cube.image.url
    player_green_amount = values.player_green
    red_cube = Cube.objects.get(name='Red Cube')
    red_cube_image = red_cube.image.url
    player_red_amount = values.player_red
    yellow_cube = Cube.objects.get(name='Yellow Cube')
    yellow_cube_image = yellow_cube.image.url
    player_yellow_amount = values.player_yellow

    data = {
        "blueCubeImage": blue_cube_image,
        "greenCubeImage": green_cube_image,
        "redCubeImage": red_cube_image,
        "yellowCubeImage": yellow_cube_image,
        "blueGloryPoint": str(player_blue_amount),
        "greenGloryPoint": str(player_green_amount),
        "redGloryPoint": str(player_red_amount),
        "yellowGloryPoint": str(player_yellow_amount),
    }

    return JsonResponse(data)
