from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import HIT_LOCATIONS, SHIPSLOCALIZATIONS
from dataset.models import Cube
from game.models import Game
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import TrackPlayerHitLocations
from game.utils.game.utilUtil import next_player
from nav.models import NavBarGame

def startPlayerTurn(request):
    """Start Player Turn."""

    data = {}

    # random colour player active
    game = Game.objects.get(number=100)
    player_colour_active = next_player()
    request.session['playerColourActive'] = player_colour_active
    player_colour = request.session['playerColourActive']
    ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)
    player_hits_locations_instance = TrackPlayerHitLocations.objects.get(player_colour=player_colour)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")

    # if any location is destroyed you cannot interact with merchant
    for hit_localisation in HIT_LOCATIONS:
        if getattr(player_hits_locations_instance, hit_localisation) == 0:
            data['playerHaveDestroyedHitLocation'] = True
            break

    for ship in SHIPSLOCALIZATIONS: # for scout action
        if ship == 'merchants_ship':
            continue
        if getattr(ship_localisation_instance, ship):
            # print(getattr(ship_localisation_instance, ship), ship_localisation_instance)
            pass

    if getattr(ship_localisation_instance, f"{player_colour}_in_port"):
        request.session['playerInPort'] = True
    else:
        request.session['playerInPort'] = False

    if getattr(ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
        data['isInTheCaribbeanSea'] = True

    data['playerInPort'] = request.session['playerInPort']
    data['playerColour'] = player_colour

    return JsonResponse(data)
