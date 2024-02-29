from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import SHIPSLOCALIZATIONS
from dataset.models import Cube
from game.models import Game
from game.models import ShipsLocalisations
from game.models import PlayersShipsCards
from game.models import TrackPlayerHitLocations
from game.utils.game.utilUtil import next_player

def startPlayerActions(request):
    """Start Player Actions."""

    data = {}

    # random colour player active
    game = Game.objects.get(number=100)
    player_colour_active = next_player()
    request.session['playerColourActive'] = player_colour_active
    player_colour = request.session['playerColourActive']
    ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)
    hit_localisation_instance = TrackPlayerHitLocations.objects.get(player_colour=player_colour)

    for ship in SHIPSLOCALIZATIONS: # for scout action
        if ship == 'merchants_ship':
            continue
        if getattr(ship_localisation_instance, ship):
            print(getattr(ship_localisation_instance, ship), ship_localisation_instance)

    if getattr(ship_localisation_instance, f"{player_colour}_in_port"):
        request.session['playerInPort'] = True
    else:
        request.session['playerInPort'] = False

    if getattr(ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
        data['isInTheCaribbeanSea'] = True

    data['playerInPort'] = request.session['playerInPort']
    data['playerColour'] = player_colour

    return JsonResponse(data)
