from django.http import JsonResponse
from dataset.models import Cube
from game.models import Game
from game.models import PlayersShipsCards
from nav.models import NavBarGame

def endCurrentAction(request):
    """Update Captain Actions Track."""

    colour = request.GET.get('colour', None)

    data = {}
    game = Game.objects.get(number=100)
    game_ships = PlayersShipsCards.objects.get(game_number=game)
    nav_bar = NavBarGame.objects.get(game_number=game)
    nav_bar.player_nav(colour)

    colour_cube = Cube.objects.get(name=colour.capitalize() + ' Cube')
    colour_cube_image = colour_cube.image.url

    if 'amountActions' not in request.session:
        player_ship = getattr(game_ships, 'player_' + colour)
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

    data['activePlayerColour'] = colour
    data["cubeImage"] = colour_cube_image
    data["amountActions"] = request.session['amountActions']

    return JsonResponse(data)