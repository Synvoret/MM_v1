import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, PLAYER_COLOURS
from game.models import Game
from game.models import PlayersGloryCards
from game.models import TrackPlayerBounties
from game.models import TrackPlayerHitLocations
from game.models import TrackPlayersShipModifications
from game.models import TrackPlayerSpecialWeapons
from game.models import TrackMerchantTokens
from game.models import GameDemandTokens
from game.models import PlayersCaptainsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import StackPlayerCargoCards
from game.models import TrackGloryPoint
from game.models import TrackPlayerGolds
from game.serializers import CargoCardSerializer


def navFlow(request):

    data = {}
    game = Game.objects.get(number=100)
    player_colour = request.session['playerColourActive']
    demand_tokens = GameDemandTokens.objects.get(game_number=game)
    missions_stack = StackMissionsCards.objects.get(game_number=game)
    player_golds = TrackPlayerGolds.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_cargo_cards_instance = StackPlayerCargoCards.objects.get(player_colour=player_colour)
    ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)

    # port 
    if request.GET.get('type_request') == 'port':        
        for mission_card in ['mission_1_card', 'mission_2_card', 'mission_3_card']:
            if getattr(missions_stack, mission_card) and (getattr(missions_stack, mission_card)).port == getattr(ship_localisation_instance, f"{player_colour}_ship"):
                data['missionInPort'] = True
        if player_captain_instance.home_port == getattr(ship_localisation_instance, f"{player_colour}_ship"): 
            data['playerHomePort'] = True

    data['playerColour'] = player_colour
    return JsonResponse(data)
