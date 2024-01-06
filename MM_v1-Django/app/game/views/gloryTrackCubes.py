from django.http import HttpResponse, JsonResponse
from dataset.models import Cube
from game.models import TrackGloryPoint


def gloryTrackCube(request):
    """Endpoint back cubes to track Glory Points."""

    blue_cube = Cube.objects.get(name='Blue Cube')
    blue_cube_image = blue_cube.image.url
    green_cube = Cube.objects.get(name='Green Cube')
    green_cube_image = green_cube.image.url
    red_cube = Cube.objects.get(name='Red Cube')
    red_cube_image = red_cube.image.url
    yellow_cube = Cube.objects.get(name='Yellow Cube')
    yellow_cube_image = yellow_cube.image.url

    values = TrackGloryPoint.objects.get(game_number=1)
    player_blue_value = values.player_blue
    player_green_value = values.player_green
    player_red_value = values.player_red
    player_yellow_value = values.player_yellow

    data = {
        "blueCubeImage": blue_cube_image,
        "greenCubeImage": green_cube_image,
        "redCubeImage": red_cube_image,
        "yellowCubeImage": yellow_cube_image,
        "playerBlue": player_blue_value,
        "playerGreen": player_green_value,
        "playerRed": player_red_value,
        "playerYellow": player_yellow_value,
    }

    return JsonResponse(data)
