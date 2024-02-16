from django.http import JsonResponse
from dataset.models import Cube
from game.models import PlayersShipsCards

def endCurrentAction(request):
    """Update Captain Actions Track."""



    # AUTOMATICLY NEXT PLAYER
    # if request.method == 'GET':

    #     data = {}

    #     colour = request.GET.get('colour', None)

    #     colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    #     colour_cube_image = colour_cube.image.url

    #     if 'amountActions' not in request.session:
    #         player_ship = getattr(PlayersShipsCards, 'player_' + colour)
    #         amount_actions = player_ship.speed
    #         request.session['amountActions'] = amount_actions
    #         request.session['currentAction'] = 0
    #     else:
    #         request.session['amountActions'] -= 1
    #         request.session['currentAction'] += 1
    #         data['currentAction'] = request.session['currentAction']
    #         if request.session['amountActions'] == 0:
    #             data['nextPlayer'] = True
    #             del request.session['amountActions']
    #             return JsonResponse(data)

    #     print(dict(request.session))

    #     data["cubeImage"] = colour_cube_image
    #     data["amountActions"] = request.session['amountActions']

    #     return JsonResponse(data)








    # NEXT PLAYER AFTER END TURN CLICK
    if request.method == 'GET':

        data = {}

        colour = request.GET.get('colour', None)
        data['activePlayerColour'] = colour

        colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
        colour_cube_image = colour_cube.image.url

        if 'amountActions' not in request.session:
            player_ship = getattr(PlayersShipsCards, 'player_' + colour)
            amount_actions = player_ship.speed
            request.session['amountActions'] = amount_actions
            request.session['currentAction'] = 0
        else:
            request.session['amountActions'] -= 1
            request.session['currentAction'] += 1
            data['currentAction'] = request.session['currentAction']
            if request.session['amountActions'] == 0: # END TURN, turn off all buttons except End Turn
                data['nextPlayer'] = True
                data["cubeImage"] = colour_cube_image
                del request.session['amountActions']
                return JsonResponse(data)

        data["cubeImage"] = colour_cube_image
        data["amountActions"] = request.session['amountActions']

        return JsonResponse(data)