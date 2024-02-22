from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import SHIPSLOCALIZATIONS
from dataset.models import Cube
from game.models import Game
from game.models import ShipsLocalisations
from game.models import PlayersShipsCards
from game.utils.game.utilUtil import next_player

def startPlayerActions(request):
    """Start Player Actions."""

    data = {}

    # random colour player active
    game = Game.objects.get(number=100)
    player_colour_active = next_player()
    request.session['playerColourActive'] = player_colour_active
    player_colour = request.session['playerColourActive']
    player_ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)

    for ship in SHIPSLOCALIZATIONS: # for scout action
        if ship == 'merchants_ship':
            continue
        if getattr(player_ship_localisation_instance, ship):
            print(getattr(player_ship_localisation_instance, ship), player_ship_localisation_instance)
        # if ship:
        #     print('JEST')

    if getattr(player_ship_localisation_instance, f"{player_colour}_in_port"):
        request.session['playerInPort'] = True
    else:
        request.session['playerInPort'] = False

    if getattr(player_ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
        data['isInTheCaribbeanSea'] = True

    data['playerInPort'] = request.session['playerInPort']
    data['playerColour'] = player_colour

    return JsonResponse(data)
