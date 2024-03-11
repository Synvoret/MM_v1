from django.http import HttpResponse, JsonResponse
from dataset.models import Cube
from game.models import Game
from game.models import TrackLoyality


def loyalityTrackCube(request):
    """Endpoint back cubes to track crew loyality."""

    colour = request.GET.get('colour', None)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    game = Game.objects.get(number=100)
    values = TrackLoyality.objects.get(game_number=game)
    if colour == 'blue':
        loyality_value = (values.player_blue).lower().replace(' ', '-')
    if colour == 'green':
        loyality_value = (values.player_green).lower().replace(' ', '-')
    if colour == 'red':
        loyality_value = (values.player_red).lower().replace(' ', '-')
    if colour == 'yellow':
        loyality_value = (values.player_yellow).lower().replace(' ', '-')

    data = {
        "cubeImage": colour_cube_image,
        "loyalityValue": loyality_value,
    }

    print(data)

    return JsonResponse(data)
