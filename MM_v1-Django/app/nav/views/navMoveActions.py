import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from board.models import SeaZone
from dataset.utils.dataset.decorators.choices import DIRECTION
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations
from nav.models import NavBarGame


@csrf_exempt
def navMoveActions(request):

    player_colour = request.session['playerColourActive']
    game = Game.objects.get(number=100)
    player_ship_localisations = ShipsLocalisations.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    nav_bar = NavBarGame.objects.get(game_number=game)
    player_nav_bar = getattr(nav_bar, f"player_{player_colour}")

    data = {}

    # WHEN CLICK "MOVES" BUTTON, CHECKING LOCALISATION for SHIP SEA ZONE or PORT
    if request.GET.get('when', None) == 'moves':
        if 'playerInPort' in player_nav_bar:
            data['playerInPort'] = True
        if 'isInTheCaribbeanSea' in player_nav_bar:
            data['isInTheCaribbeanSea'] = True


    if request.GET.get('when', None) == 'back':
        if 'playerInPort' in player_nav_bar:
            data['playerInPort'] = True
        if 'isInTheCaribbeanSea' in player_nav_bar:
            data['isInTheCaribbeanSea'] = True


    # WHEN PLAYER move TO PORT or FROM PORT or TO SEA ZONE
    if request.method == 'POST':
        player_ship_unit_instance = getattr(PlayersShipsCards.objects.get(game_number=game), f"player_{player_colour}")
        player_ship_unit = player_ship_unit_instance.ship
        player_ship_position = getattr(player_ship_localisations, player_colour + '_ship')

        if request.POST.get('when') == 'to sea zone':
            actual_sea_zone = SeaZone.objects.get(sea_zone_name=player_ship_position)
            for direction in DIRECTION:
                destination = getattr(actual_sea_zone, f"{direction[0].lower()}_direction")
                if destination:
                    data[direction[0].lower()] = destination

        player_ship_localisations.save()
        data['playerShipUnit'] = player_ship_unit.lower()
        data['playerDestination'] = player_ship_position.lower().replace(' ', '-')
        data['playerColour'] = player_colour

    return JsonResponse(data)
