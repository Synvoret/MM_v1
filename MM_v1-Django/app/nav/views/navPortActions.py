import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, LOYALITY, PLAYER_COLOURS
from game.models import Game
from game.models import GameDemandTokens
from game.models import PlayersCaptainsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import StackPlayerCargoCards
from game.models import TrackFavors
from game.models import TrackGloryPoint
from game.models import TrackLoyality
from game.models import TrackPlayerGolds
from game.serializers import CargoCardSerializer
from nav.models import NavBarGame


@csrf_exempt
def navPortActions(request):
    """Function is responsible for Port Actions."""

    data = {}
    game = Game.objects.get(number=100)
    player_colour = request.session['playerColourActive']
    demand_tokens = GameDemandTokens.objects.get(game_number=game)
    missions_stack = StackMissionsCards.objects.get(game_number=game)
    player_golds = TrackPlayerGolds.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_cargo_cards_instance = StackPlayerCargoCards.objects.get(player_colour=player_colour)
    ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)
    favours = TrackFavors.objects.get(game_number=game)
    loyality = TrackLoyality.objects.get(game_number=game)
    nav_bar = NavBarGame.objects.get(game_number=game)
    player_nav_bar = getattr(nav_bar, f"player_{player_colour}")


    # GET method
    if request.method == 'GET':

        # port
        if request.GET.get('when') == 'port':
            # sell goods ?
            if 'sellGoods' in player_nav_bar:
                data['sellGoods'] = True
            else:
                nav_bar.player_nav(player_colour, 'sellGoods')
            for mission_card in ['mission_1_card', 'mission_2_card', 'mission_3_card']:
                if getattr(missions_stack, mission_card) and (getattr(missions_stack, mission_card)).port == getattr(ship_localisation_instance, f"{player_colour}_ship"):
                    data['missionInPort'] = True
            if player_captain_instance.home_port == getattr(ship_localisation_instance, f"{player_colour}_ship"): 
                data['captainHomePort'] = True
            if getattr(player_golds, f"player_{player_colour}") < 2 or getattr(favours, f"player_{player_colour}") == 5 or 'getFavour' in player_nav_bar:
                data['cantGetFavour'] = True
            if getattr(player_golds, f"player_{player_colour}") < 2 or getattr(loyality, f"player_{player_colour}") == 'Fierce Loyality' or 'raiseLoyality' in player_nav_bar:  # this is max at loyality track
                data['cantChangeLoyality'] = True

        # visit shipyard 
        if request.GET.get('when') == 'visit shipyard':
            print('VISIT SHIPYARD')

        if request.GET.get('when') == 'raise loyality':
            if 'raiseLoyality' in player_nav_bar:
                data['cantChangeLoyality'] = True
        
        if request.GET.get('when') == 'get favour':
            if 'getFavour' in player_nav_bar:
                data['getFavour'] = True

        if request.GET.get('when') == 'back to port':
            data['sellGoods'] = True

    # POST method
    if request.method == 'POST':
        pass

    data['playerColour'] = player_colour
    return JsonResponse(data)
