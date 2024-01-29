from django.http import JsonResponse, HttpResponse
from dataset.models import Cube
from game.models import PlayersShipsCards

def updateCaptainActions(request):
    """Update Captain Actions Track."""

    if request.method == 'GET':

        data = {}

        colour = request.GET.get('colour', None)

        colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
        colour_cube_image = colour_cube.image.url

        if 'amountActions' not in request.session:
            player_ship = getattr(PlayersShipsCards, 'player_' + colour)
            amount_actions = player_ship.speed
            request.session['amountActions'] = amount_actions
        else:
            request.session['amountActions'] -= 1
            if request.session['amountActions'] == 0:
                data['nextPlayer'] = True
                del request.session['amountActions']
                return JsonResponse(data)

        print(dict(request.session))

        data["cubeImage"] = colour_cube_image
        data["amountActions"] = request.session['amountActions']

        return JsonResponse(data)
