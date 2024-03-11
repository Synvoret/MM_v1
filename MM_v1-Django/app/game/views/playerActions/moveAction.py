import random
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from board.models import SeaZone
from dataset.utils.dataset.decorators.choices import ALLOWEDDESTINATIONS, DIRECTION
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations


@csrf_exempt
def moveAction(request):

    player_colour = request.session['playerColourActive']
    game = Game.objects.get(number=100)
    player_ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")

    data = {}

    # WHEN CLICK "MOVES" BUTTON, CHECKING LOCALISATION for SHIP SEA ZONE or PORT
    if request.GET.get('type_request', None) == 'moves':
        if getattr(player_ship_localisation_instance, f"{player_colour}_in_port"):
            data['unitInPort'] = True
        if getattr(player_ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
            data['isInTheCaribbeanSea'] = True


    if request.GET.get('type_request', None) == 'back':
        data['playerInPort'] = getattr(player_ship_localisation_instance, f"{player_colour}_in_port")
        if getattr(player_ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
            data['isInTheCaribbeanSea'] = True


    # WHEN PLAYER move TO PORT or FROM PORT or TO SEA ZONE
    if request.method == 'POST':
        player_ship_unit_instance = getattr(PlayersShipsCards.objects.get(game_number=game), f"player_{player_colour}")
        player_ship_unit = player_ship_unit_instance.ship
        player_ship_position = getattr(player_ship_localisation_instance, player_colour + '_ship')

        if request.POST.get('type_request') == 'to port':
            setattr(player_ship_localisation_instance, f"{player_colour}_in_port", True)

        if request.POST.get('type_request') == 'from port':
            setattr(player_ship_localisation_instance, f"{player_colour}_in_port", False)
            request.session['playerInPort'] = False

        if request.POST.get('type_request') == 'to sea zone':
            actual_sea_zone = SeaZone.objects.get(sea_zone_name=player_ship_position)
            for direction in DIRECTION:
                destination = getattr(actual_sea_zone, f"{direction[0].lower()}_direction")
                if destination:
                    data[direction[0].lower()] = destination

        if request.POST.get('type_request') in ALLOWEDDESTINATIONS:
            setattr(player_ship_localisation_instance, player_colour + '_ship', request.POST.get('type_request'))
            player_ship_position = getattr(player_ship_localisation_instance, player_colour + '_ship')
            if request.session['amountActions'] == 1:
                data['lastAction'] = True

        player_ship_localisation_instance.save()
        data['playerShipUnit'] = player_ship_unit.lower()
        data['playerDestination'] = player_ship_position.lower().replace(' ', '-')
        data['playerColour'] = player_colour

    return JsonResponse(data)
