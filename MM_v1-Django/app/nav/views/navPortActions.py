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


    # GET method
    if request.method == 'GET':

        # port 
        if request.GET.get('when') == 'port':        
            for mission_card in ['mission_1_card', 'mission_2_card', 'mission_3_card']:
                if getattr(missions_stack, mission_card) and (getattr(missions_stack, mission_card)).port == getattr(ship_localisation_instance, f"{player_colour}_ship"):
                    data['missionInPort'] = True
            if player_captain_instance.home_port == getattr(ship_localisation_instance, f"{player_colour}_ship"): 
                data['playerHomePort'] = True
            if getattr(player_golds, f"player_{player_colour}") < 2 or getattr(favours, f"player_{player_colour}") == 5:
                data['cantGetFavour'] = True
            if getattr(player_golds, f"player_{player_colour}") < 2 or getattr(loyality, f"player_{player_colour}") == 'Fierce Loyality':  # this is max at loyality track
                data['cantChangeLoyality'] = True

        # visit shipyard 
        if request.GET.get('when') == 'visit shipyard':
            print('VISIT SHIPYARD')

    # POST method
    if request.method == 'POST':
        pass

    data['playerColour'] = player_colour
    return JsonResponse(data)
