import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from board.models import SeaZone
from dataset.utils.dataset.decorators.choices import BOUNTIES, DIRECTION
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations
from game.models import TrackPlayerBounties
from nav.models import NavBarGame


@csrf_exempt
def navMoveActions(request):

    player_colour = request.session['playerColourActive']
    game = Game.objects.get(number=100)
    game_ship_localisations = ShipsLocalisations.objects.get(game_number=game)
    game_captains = PlayersCaptainsCards.objects.get(game_number=game)
    game_bounties = TrackPlayerBounties.objects.get(game_number=game)
    player_bounties = getattr(game_bounties, f"player_{player_colour}") # list()
    player_captain = getattr(game_captains, f"player_{player_colour}")
    nav_bar_game = NavBarGame.objects.get(game_number=game)
    player_nav_bar = getattr(nav_bar_game, f"player_{player_colour}")

    player_ship_position = getattr(game_ship_localisations, player_colour + '_ship')
    actual_sea_zone = SeaZone.objects.get(sea_zone_name=player_ship_position)

    data = {}

    # WHEN CLICK "MOVES" BUTTON, CHECKING LOCALISATION for SHIP SEA ZONE or PORT
    if request.GET.get('when', None) == 'moves':
        if 'playerInPort' in player_nav_bar:
            data['playerInPort'] = True
        if 'isInTheCaribbeanSea' in player_nav_bar:
            data['isInTheCaribbeanSea'] = True
        for bounty in BOUNTIES: # if any bounties, player can't arrive to bounty port
            if bounty in player_bounties and bounty == actual_sea_zone.port_nationality:
                data[f"bountyPortNationality"] = True


    if request.GET.get('when', None) == 'back':
        if 'playerInPort' in player_nav_bar:
            data['playerInPort'] = True
        if 'isInTheCaribbeanSea' in player_nav_bar:
            data['isInTheCaribbeanSea'] = True


    # WHEN PLAYER move TO PORT or FROM PORT or TO SEA ZONE
    if request.method == 'POST':
        player_ship_unit_instance = getattr(PlayersShipsCards.objects.get(game_number=game), f"player_{player_colour}")
        player_ship_unit = player_ship_unit_instance.ship

        if request.POST.get('when') == 'to sea zone':
            for direction in DIRECTION:
                destination = getattr(actual_sea_zone, f"{direction[0].lower()}_direction")
                if destination:
                    data[direction[0].lower()] = destination

        game_ship_localisations.save()
        data['playerShipUnit'] = player_ship_unit.lower()
        data['playerDestination'] = player_ship_position.lower().replace(' ', '-')
        data['playerColour'] = player_colour

    return JsonResponse(data)
